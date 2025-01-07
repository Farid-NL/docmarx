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


def add_vulnerability(language: str, vulnerability_name: str) -> dict | bool:
    def get_name_of(element: dict) -> str:
        return list(element.keys())[0]

    yaml_data = load_mkdocs_yaml()

    nav_element = yaml_data["nav"]
    md_file = f"{language.lower()}/{vulnerability_name.lower().replace(" ", "-")}.md"

    for section in nav_element:
        language_key = get_name_of(section)

        if language_key.lower() == language.lower():
            existing_vulnerabilities = [
                get_name_of(vulnerability).lower()
                for vulnerability in section[language_key]
            ]

            if vulnerability_name.lower() not in existing_vulnerabilities:
                section[language].append({vulnerability_name: md_file})
                return nav_element

            return False

    nav_element.append({language: [{vulnerability_name: md_file}]})
    return nav_element


def remove_vulnerability(language: str, vulnerability_name: str) -> dict | bool:
    def get_name_of(element: dict) -> str:
        return list(element.keys())[0]

    yaml_data = load_mkdocs_yaml()
    nav_element = yaml_data["nav"]

    for section in nav_element:
        if language in section:
            for index, vulnerability in enumerate(section[language]):
                vulnerability_identifier = get_name_of(vulnerability)
                if vulnerability_identifier == vulnerability_name:
                    section[language].pop(index)
            return nav_element

    return False


def add_vulnerability_file(
    language: str, vulnerability_name: str, severity: str
) -> Path | bool:
    vuln_file_name = vulnerability_name.lower().replace(" ", "-") + ".md"
    vuln_file_dir = Path(__file__).resolve().parents[1] / "docs" / language.lower()
    tmpl_path = Path(__file__).resolve().parents[1] / "vulnerability.tmpl"

    vuln_path = vuln_file_dir / vuln_file_name
    if vuln_path.exists():
        return False

    vuln_file_dir.mkdir(parents=True, exist_ok=True)
    with open(tmpl_path, "r") as tmpl_file, open(vuln_path, "w+") as vuln_file:
        tmpl_content = tmpl_file.read().replace("{{{language}}}", language)
        if severity:
            tmpl_content = tmpl_content.replace("{{{severity}}}", f"- {severity}")
        else:
            tmpl_content = tmpl_content.replace("{{{severity}}}", "#- Baja")
        vuln_file.write(tmpl_content)

    return vuln_path


def remove_vulnerability_file(language: str, vulnerability_name: str):
    vuln_file_name = vulnerability_name.lower().replace(" ", "-") + ".md"
    vuln_file_dir = Path(__file__).resolve().parents[1] / "docs" / language.lower()

    vuln_path = vuln_file_dir / vuln_file_name
    if not vuln_path.exists():
        return False

    vuln_path.unlink()
    return vuln_path


def update_mkdocs_nav(nav_data: str):
    with open(MKDOCS_YAML_PATH, "r") as mkdocs_file:
        content = mkdocs_file.readlines()

    # Identifica la colección nav en mkdocs.yaml
    nav_section_start = None
    nav_section_end = None
    for line_number, line in enumerate(content):
        # Inicio de la colección
        if re.match(r"^nav:", line):
            nav_section_start = line_number
        # Fin de la colección
        elif nav_section_start is not None and re.match(r"^\S", line):
            nav_section_end = line_number
            break

    # Maneja el caso en el que nav sea el último nodo en mkdocs.yml
    nav_section_end = nav_section_end or len(content)

    # Actualiza la colección nav en mkdocs.yaml
    content = content[:nav_section_start] + [nav_data] + content[nav_section_end:]

    # Escribe los cambios realizados mkdocs.yaml
    with open(MKDOCS_YAML_PATH, "w") as mkdocs_file:
        mkdocs_file.writelines(content)


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
        nav_sorted = sort_vulnerabilities(is_nav_modified)
        update_mkdocs_nav(nav_sorted)
        print("Se agregó la vulnerabilidad al archivo mkdocs.yml")
    else:
        print("No se agregó la vulnerabilidad al archivo mkdocs.yml")

    severity = "Alta" if alta else "Media" if media else "Baja" if baja else None
    is_file_created = add_vulnerability_file(language, vulnerability, severity)
    if is_file_created:
        print(f"Se creó el archivo asociado en '{is_file_created}'")
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
        print(f"Se removió el archivo asociado '{is_file_removed}'")
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
