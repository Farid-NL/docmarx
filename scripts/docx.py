import copy
import re
import textwrap
from pathlib import Path

import click
import yaml


class IndentDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(IndentDumper, self).increase_indent(flow, False)


def sort_vulnerabilities(yaml_data: dict) -> str:
    for item in yaml_data:
        for key in item:
            if key != "Inicio":
                item[key] = sorted(item[key], key=lambda x: list(x.keys())[0])

    sorted_yaml = yaml.dump(
        yaml_data, Dumper=IndentDumper, allow_unicode=True, sort_keys=False
    )
    sorted_yaml = textwrap.indent(sorted_yaml, " " * 2)

    return f"nav:\n{sorted_yaml}"


def add_vulnerability(
    yaml_path: Path, language: str, vulnerability_name: str
) -> tuple[bool, dict] | bool:
    # Carga mkdocs.yml
    with open(yaml_path, "r") as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)

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


def remove_vulnerability(
    yaml_path: Path, language: str, vulnerability_name: str
) -> dict | bool:
    # Carga mkdocs.yml
    with open(yaml_path, "r") as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)

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
    language: str, vulnerability_name: str
) -> tuple[bool, Path] | bool:
    language = language.lower()
    md_file = vulnerability_name.lower().replace(" ", "-") + ".md"
    md_file_dir = Path(__file__).resolve().parents[1] / "docs" / language

    md_path = md_file_dir / md_file
    if not md_path.exists():
        md_file_dir.mkdir(parents=True, exist_ok=True)
        with open(md_path, "w+") as md_file:
            md_file.write(f"---\nicon: material/language-{language}\n---\n")
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


def update_mkdocs_yaml(new_nav_data: str, yaml_path: Path):
    with open(yaml_path, "r") as yaml_file:
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
    with open(yaml_path, "w", encoding="utf-8") as yaml_file:
        yaml_file.writelines(content)


@click.group()
def cli():
    """Docmarx CLI - Helper for vulnerabilities documentation"""


@cli.command()
@click.argument("language")
@click.argument("vulnerability_name")
def add(language: str, vulnerability_name: str):
    # Ubica el archivo mkdocs.yml dentro del proyecto
    project_root = Path(__file__).resolve().parents[1]
    mkdocs_yml = project_root / "mkdocs.yml"

    is_nav_modified = add_vulnerability(mkdocs_yml, language, vulnerability_name)
    if is_nav_modified:
        nav_sorted = sort_vulnerabilities(is_nav_modified[1])
        update_mkdocs_yaml(nav_sorted, mkdocs_yml)
        print("Se agregó la vulnerabilidad al archivo mkdocs.yml")
    else:
        print("No se agregó la vulnerabilidad al archivo mkdocs.yml")

    is_file_created = add_vulnerability_file(language, vulnerability_name)
    if is_file_created:
        print(f"Se creó el archivo asociado en '{is_file_created[1]}'")
    else:
        print("No se creo un archivo asociado a la vulnerabilidad")


@cli.command()
@click.argument("language")
@click.argument("vulnerability_name")
def remove(language: str, vulnerability_name: str):
    # Ubica el archivo mkdocs.yml dentro del proyecto
    project_root = Path(__file__).resolve().parents[1]
    mkdocs_yml = project_root / "mkdocs.yml"

    is_nav_modified = remove_vulnerability(mkdocs_yml, language, vulnerability_name)
    if is_nav_modified:
        nav_sorted = sort_vulnerabilities(is_nav_modified)
        update_mkdocs_yaml(nav_sorted, mkdocs_yml)
        print("Se removió la vulnerabilidad del archivo mkdocs.yml")
    else:
        print("No se removió la vulnerabilidad del archivo mkdocs.yml")

    is_file_removed = remove_vulnerability_file(language, vulnerability_name)
    if is_file_removed:
        print(f"Se removió el archivo asociado '{is_file_removed[1]}'")
    else:
        print("No se removió un archivo asociado a la vulnerabilidad")


if __name__ == "__main__":
    cli()
