"""Read Package version file functions."""


def get_package_version(package_path: str) -> str:
    """Read the package's VERSION file.

    Args:
        package_path (str): Package's root directory path.

    Returns:
        str: Version string.
    """
    try:
        with open(f"{package_path}/VERSION", "r", encoding="utf-8") as file:
            version = file.readline().strip()
            return version
    except FileNotFoundError:
        return "VERSION file not found."
