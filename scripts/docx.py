import re
import textwrap
from pathlib import Path

import click
import yaml

ROOT_PATH = Path(__file__).resolve().parents[1]
MKDOCS_YAML_PATH = ROOT_PATH / "mkdocs.yml"


def load_mkdocs_yaml():
    def constructor_ignore_python_objects(loader, prefix, node):
        return node.tag.replace("tag:yaml.org,2002:", "!!")

    with open(MKDOCS_YAML_PATH, "r") as yaml_file:
        yaml.SafeLoader.add_multi_constructor(
            "tag:yaml.org,2002:python/name:", constructor_ignore_python_objects
        )
        yaml_data = yaml.safe_load(yaml_file)
    return yaml_data


def get_language_dir(language: str) -> str:
    languages_dict = {
        "c++": "cpp",
        "cpp": "cpp",
        "csharp": "cs",
        "c#": "cs",
        "cs": "cs",
        "javascript": "js",
        "js": "js",
        "python": "py",
        "py": "py",
    }

    if language.lower() in languages_dict:
        return languages_dict[language.lower()]
    else:
        return language.lower()


def get_language_name_for_nav(language: str) -> str:
    language = get_language_dir(language)
    languages_dict = {
        "cpp": "C++",
        "cs": "C#",
        "js": "Javascript",
        "py": "Python",
        "php": "PHP",
    }

    if language in languages_dict:
        return languages_dict[language]
    else:
        return language.capitalize()


def exit_if_nav_not_in_yaml(yaml_data):
    if "nav" not in yaml_data:
        click.echo("La sección 'nav' no existe en el archivo mkdocs.yml.", err=True)
        exit(1)


def sort_vulnerabilities(nav_element: list) -> str:
    class IndentDumper(yaml.Dumper):
        """Clase auxiliar para incrementar la indentación"""

        def increase_indent(self, flow=False, indentless=False):
            return super(IndentDumper, self).increase_indent(flow, False)

    def get_vulnerability_name(vulnerability: dict) -> str:
        return list(vulnerability.keys())[0]

    for section in nav_element:
        for section_name in section:
            if section_name != "Docmarx":
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


def add_vulnerability(language: str, vulnerability_name: str) -> list | bool:
    def get_name_of(element: dict) -> str:
        return list(element.keys())[0]

    yaml_data = load_mkdocs_yaml()
    exit_if_nav_not_in_yaml(yaml_data)

    nav_element = yaml_data["nav"]
    md_file = f"{get_language_dir(language)}/{vulnerability_name.lower().replace(" ", "-")}.md"

    language = get_language_name_for_nav(language)
    for section in nav_element:
        language_key = get_name_of(section)

        if language_key == language:
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


def remove_vulnerability(language: str, vulnerability_name: str) -> list | str:
    def get_name_of(element: dict) -> str:
        return list(element.keys())[0]

    yaml_data = load_mkdocs_yaml()
    exit_if_nav_not_in_yaml(yaml_data)

    nav_element = yaml_data["nav"]
    language = get_language_name_for_nav(language)
    for section in nav_element:
        if language in section:
            for index, vulnerability in enumerate(section[language]):
                vulnerability_identifier = get_name_of(vulnerability)
                if vulnerability_identifier == vulnerability_name:
                    section[language].pop(index)
                    return nav_element

            return f"Vulnerabilidad '{vulnerability_name}' no existe"

    return f"Lenguaje '{language}' no existe"


def add_vulnerability_file(
    language: str, vulnerability_name: str, severity: str
) -> Path | bool:
    vuln_file_name = vulnerability_name.lower().replace(" ", "-") + ".md"
    vuln_file_dir = ROOT_PATH / "docs" / get_language_dir(language)
    tmpl_path = ROOT_PATH / "vulnerability.tmpl"

    vuln_path = vuln_file_dir / vuln_file_name
    if vuln_path.exists():
        return False

    vuln_file_dir.mkdir(parents=True, exist_ok=True)
    with open(tmpl_path, "r") as tmpl_file, open(vuln_path, "w+") as vuln_file:
        language = get_language_name_for_nav(language)
        tmpl_content = tmpl_file.read().replace("{{{language}}}", language)
        if severity:
            tmpl_content = tmpl_content.replace("{{{severity}}}", f"- {severity}")
        else:
            tmpl_content = tmpl_content.replace("{{{severity}}}", "#- Alta|Media|Baja")
        vuln_file.write(tmpl_content)

    return vuln_path.relative_to(ROOT_PATH)


def remove_vulnerability_file(language: str, vulnerability_name: str):
    vuln_file_name = vulnerability_name.lower().replace(" ", "-") + ".md"
    vuln_file_dir = ROOT_PATH / "docs" / get_language_dir(language)

    vuln_path = vuln_file_dir / vuln_file_name
    if not vuln_path.exists():
        return False

    vuln_path.unlink()
    return vuln_path.relative_to(ROOT_PATH)


def update_mkdocs_nav(nav_data: str):
    def find_nav_section(nav_content):
        """Localiza el número de línea inicial y final de la sección 'nav' en mkdocs.yml"""
        start = None
        end = None

        for line_number, line in enumerate(nav_content):
            if re.match(r"^nav:", line):
                start = line_number
            elif start is not None and re.match(r"^\S", line):
                end = line_number
                break

        # Maneja el caso en el que nav sea el último nodo en mkdocs.yml
        return start, end or len(nav_content)

    with open(MKDOCS_YAML_PATH, "r") as mkdocs_file:
        content = mkdocs_file.readlines()

    nav_start, nav_end = find_nav_section(content)
    updated_content = content[:nav_start] + [nav_data] + content[nav_end:]

    with open(MKDOCS_YAML_PATH, "w") as mkdocs_file:
        mkdocs_file.writelines(updated_content)


@click.group()
def cli():
    """Docmarx CLI - Helper for vulnerabilities documentation"""


@cli.command()
@click.argument("language")
@click.argument("vulnerability")
@click.option("--alta", "-a", is_flag=True, help="Set severity to high")
@click.option("--media", "-m", is_flag=True, help="Set severity to medium")
@click.option("--baja", "-b", is_flag=True, help="Set severity to low")
def add(language: str, vulnerability: str, alta: bool, media: bool, baja: bool):
    """Add a new vulnerability to be documented.

    Note: Only one option can be used at a time or none at all.
    """
    num_flags_activated = alta + media + baja
    if num_flags_activated not in (0, 1):
        click.echo("Solo una opción puede estar activa a la vez.", err=True)
        exit(1)

    is_nav_modified = add_vulnerability(language, vulnerability)
    if is_nav_modified:
        nav_sorted = sort_vulnerabilities(is_nav_modified)
        update_mkdocs_nav(nav_sorted)

        click.secho(f"{vulnerability}: ", fg="blue")
        click.echo(f"  {click.style("✓", fg="green")} mkdocs.yml actualizado")
    else:
        click.secho(f"{vulnerability}: ", fg="blue", nl=False)
        click.secho("Ya existe", fg="red")
        click.echo(f"  {click.style("x", fg="red")} mkdocs.yml sin cambios")

    severity = "Alta" if alta else "Media" if media else "Baja" if baja else None
    is_file_created = add_vulnerability_file(language, vulnerability, severity)
    if is_file_created:
        click.echo(f"  {click.style("✓", fg="green")} archivo creado")
    else:
        click.echo(f"  {click.style("x", fg="red")} archivo no creado")


@cli.command()
@click.argument("language")
@click.argument("vulnerability")
def remove(language: str, vulnerability: str):
    """Remove a vulnerability.

    Note: VULNERABILITY_NAME must be exactly as presented in mkdocs.yml
    """
    is_nav_modified = remove_vulnerability(language, vulnerability)
    if type(is_nav_modified) is list:
        nav_sorted = sort_vulnerabilities(is_nav_modified)
        update_mkdocs_nav(nav_sorted)

        click.secho(f"{vulnerability}:", fg="blue")
        click.echo(f"  {click.style("✓", fg="green")} mkdocs.yml actualizado")
    else:
        click.secho(f"{vulnerability}: ", fg="blue", nl=False)
        click.secho(is_nav_modified, fg="red")
        click.echo(f"  {click.style("x", fg="red")} mkdocs.yml sin cambios")

    is_file_removed = remove_vulnerability_file(language, vulnerability)
    if is_file_removed:
        click.echo(f"  {click.style("✓", fg="green")} archivo removido")
    else:
        click.echo(f"  {click.style("x", fg="red")} archivo no removido")


@cli.command()
def sort():
    """Sort the vulnerabilities in mkdocs.yml."""
    yaml_data = load_mkdocs_yaml()
    exit_if_nav_not_in_yaml(yaml_data)

    nav_sorted = sort_vulnerabilities(yaml_data["nav"])
    update_mkdocs_nav(nav_sorted)


if __name__ == "__main__":
    cli()
