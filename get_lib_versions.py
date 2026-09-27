import importlib.metadata
from pathlib import Path

PACKAGES = [
    "langchain",
    "langchain_core",
    "python-dotenv",
    "streamlit",
]

REQUIREMENTS_FILE = Path(__file__).resolve().parent / "requirements.txt"


def normalize_package_name(requirement_line):
    requirement = requirement_line.strip()
    if not requirement or requirement.startswith("#"):
        return None
    return requirement.split("==", 1)[0].split(">=", 1)[0].split("<=", 1)[0].split("~=", 1)[0].split("!=", 1)[0].strip()


def get_installed_requirements(packages):
    lines = []
    for pkg in packages:
        try:
            version = importlib.metadata.version(pkg)
        except importlib.metadata.PackageNotFoundError:
            print(f"{pkg}: Not installed")
            continue

        requirement = f"{pkg}=={version}"
        lines.append(requirement)
        print(requirement)

    return lines


def update_requirements_file(file_path, packages):
    installed_lines = get_installed_requirements(packages)
    installed_map = {line.split("==", 1)[0]: line for line in installed_lines}

    existing_lines = []
    if file_path.exists():
        existing_lines = file_path.read_text(encoding="utf-8").splitlines()

    final_lines = []
    seen = set()

    for line in existing_lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            final_lines.append(line)
            continue

        package_name = normalize_package_name(stripped)
        if package_name in packages:
            if package_name in installed_map and package_name not in seen:
                final_lines.append(installed_map[package_name])
                seen.add(package_name)
            continue

        final_lines.append(line)

    for package_name in packages:
        if package_name in installed_map and package_name not in seen:
            final_lines.append(installed_map[package_name])
            seen.add(package_name)

    file_path.write_text("\n".join(final_lines) + ("\n" if final_lines else ""), encoding="utf-8")
    return final_lines


if __name__ == "__main__":
    update_requirements_file(REQUIREMENTS_FILE, PACKAGES)
