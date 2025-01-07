import copy
import re
import textwrap
from pathlib import Path

import click
import yaml

MKDOCS_YAML_PATH = Path(__file__).resolve().parents[1] / "mkdocs.yml"


def load_mkdocs_yaml():
    with open(MKDOCS_YAML_PATH, "r") as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)
    return yaml_data


# Funciones
def sort_vulnerabilities(nav_element: dict) -> str:
    class IndentDumper(yaml.Dumper):
        """Clase auxiliar para incrementar la indentación"""

        def increase_indent(self, flow=False, indentless=False):
            return super(IndentDumper, self).increase_indent(flow, False)

    def get_vulnerability_name(vulnerability: dict) -> str:
        return list(vulnerability.keys())[0]

    for section in nav_element:
        for section_name in section:
            if section_name != "Inicio":
                # Ordena las vulnerabilidades alfabéticamente
                section[section_name] = sorted(
                    section[section_name],
                    key=get_vulnerability_name,
                )

    # Incrementa la indentación del arreglo de vulnerabilidades
    sorted_nav_yaml = yaml.dump(
        nav_element, Dumper=IndentDumper, allow_unicode=True, sort_keys=False
    )
    # Sin esto, el elemento nav de mkdocs.yaml quedaría con una indentación incorrecta
    sorted_nav_yaml = textwrap.indent(sorted_nav_yaml, " " * 2)

    return f"nav:\n{sorted_nav_yaml}"


def add_vulnerability(
    language: str, vulnerability_name: str
) -> tuple[bool, dict] | bool:
    # Carga mkdocs.yml
    yaml_data = load_mkdocs_yaml()

    original_nav_element = copy.deepcopy(yaml_data["nav"])
    nav_element = yaml_data["nav"]
    md_file = f"{language.lower()}/{vulnerability_name.lower().replace(" ", "-")}.md"

    for item in nav_element:
        language_key = next(iter(item))
        if language_key.lower() == language.lower():
            if not any(
                vulnerability_name.lower() == next(iter(current_vulnerability)).lower()
                for current_vulnerability in item[language_key]
            ):
                item[language].append({vulnerability_name: md_file})

            return False if nav_element == original_nav_element else (True, nav_element)

    nav_element.append({language: [{vulnerability_name: md_file}]})

    return True, nav_element


def remove_vulnerability(language: str, vulnerability_name: str) -> dict | bool:
    # Carga mkdocs.yml
    yaml_data = load_mkdocs_yaml()

    nav_element = yaml_data["nav"]

    for item in nav_element:
        if language in item:
            for index, current_vulnerability in enumerate(item[language]):
                vulnerability_key = next(iter(current_vulnerability))
                if vulnerability_key == vulnerability_name:
                    item[language].pop(index)
            return nav_element

    return False


def add_vulnerability_file(
    language: str, vulnerability_name: str, severity: str
) -> tuple[bool, Path] | bool:
    language_lowercase = language.lower()
    md_file = vulnerability_name.lower().replace(" ", "-") + ".md"
    md_file_dir = Path(__file__).resolve().parents[1] / "docs" / language_lowercase
    template_path = Path(__file__).resolve().parents[1] / "vulnerability.tmpl"

    md_path = md_file_dir / md_file
    if not md_path.exists():
        md_file_dir.mkdir(parents=True, exist_ok=True)
        with open(md_path, "w+") as md_file, open(template_path, "r") as template_file:
            tmpl_content = template_file.read().replace("{{{language}}}", language)
            if severity:
                tmpl_content = tmpl_content.replace("{{{severity}}}", f"- {severity}")
            else:
                tmpl_content = tmpl_content.replace("{{{severity}}}", "#- Baja")
            md_file.write(tmpl_content)
        return True, md_path
    else:
        return False


def remove_vulnerability_file(language: str, vulnerability_name: str):
    language = language.lower()
    md_file = vulnerability_name.lower().replace(" ", "-") + ".md"
    md_file_dir = Path(__file__).resolve().parents[1] / "docs" / language

    md_path = md_file_dir / md_file
    if md_path.exists():
        md_path.unlink()
        return True, md_path
    else:
        return False


def update_mkdocs_nav(new_nav_data: str):
    with open(MKDOCS_YAML_PATH, "r") as yaml_file:
        content = yaml_file.readlines()

    # Identifica la sección nav de mkdocs.yaml
    nav_section_start = None
    nav_section_end = None
    for line_number, line in enumerate(content):
        # Inicio de la sección
        if re.match(r"^nav:", line):
            nav_section_start = line_number
        # Fin de la sección
        elif nav_section_start is not None and re.match(r"^\S", line):
            nav_section_end = line_number
            break

    # Reemplaza la sección nav de mkdocs.yaml
    nav_section_end = nav_section_end or len(content)
    content = content[:nav_section_start] + [new_nav_data] + content[nav_section_end:]

    # Actualiza el archivo mkdocs.yaml
    with open(MKDOCS_YAML_PATH, "w", encoding="utf-8") as yaml_file:
        yaml_file.writelines(content)


@click.group()
def cli():
    """Docmarx CLI - Helper for vulnerabilities documentation"""


@cli.command()
@click.argument("language")
@click.argument("vulnerability")
@click.option(
    "--alta",
    "-a",
    is_flag=True,
    help="Set severity to high",
)
@click.option(
    "--media",
    "-m",
    is_flag=True,
    help="Set severity to medium",
)
@click.option(
    "--baja",
    "-b",
    is_flag=True,
    help="Set severity to low",
)
def add(language: str, vulnerability: str, alta: bool, media: bool, baja: bool):
    """Add a new vulnerability to be documented.

    Note: Only one option can be used at a time or none at all.
    """
    num_flags_activated = alta + media + baja
    if num_flags_activated not in (0, 1):
        print("Solo una bandera puede estar activa a la vez.")
        exit(1)

    is_nav_modified = add_vulnerability(language, vulnerability)
    if is_nav_modified:
        nav_sorted = sort_vulnerabilities(is_nav_modified[1])
        update_mkdocs_nav(nav_sorted)
        print("Se agregó la vulnerabilidad al archivo mkdocs.yml")
    else:
        print("No se agregó la vulnerabilidad al archivo mkdocs.yml")

    severity = "Alta" if alta else "Media" if media else "Baja" if baja else None
    is_file_created = add_vulnerability_file(language, vulnerability, severity)
    if is_file_created:
        print(f"Se creó el archivo asociado en '{is_file_created[1]}'")
    else:
        print("No se creo un archivo asociado a la vulnerabilidad")


@cli.command()
@click.argument("language")
@click.argument("vulnerability")
def remove(language: str, vulnerability: str):
    """Remove a vulnerability.

    Note: VULNERABILITY_NAME must be exactly as presented in mkdocs.yml
    """
    is_nav_modified = remove_vulnerability(language, vulnerability)
    if is_nav_modified:
        nav_sorted = sort_vulnerabilities(is_nav_modified)
        update_mkdocs_nav(nav_sorted)
        print("Se removió la vulnerabilidad del archivo mkdocs.yml")
    else:
        print("No se removió la vulnerabilidad del archivo mkdocs.yml")

    is_file_removed = remove_vulnerability_file(language, vulnerability)
    if is_file_removed:
        print(f"Se removió el archivo asociado '{is_file_removed[1]}'")
    else:
        print("No se removió un archivo asociado a la vulnerabilidad")


@cli.command()
def sort():
    """Sort the vulnerabilities presented in the nav section of mkdocs.yml."""
    yaml_data = load_mkdocs_yaml()

    nav_sorted = sort_vulnerabilities(yaml_data["nav"])
    update_mkdocs_nav(nav_sorted)


if __name__ == "__main__":
    cli()
