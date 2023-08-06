"""pypi utility functions"""

from requests import get


def check_pypi_availability(pkg_name: str) -> bool:
    """check PyPi package name availability

    Args:
        pkg_name (str): package name to be checked

    Examples:
        >>> check_pypi_availability('ktemplate')
        False

        >>> check_pypi_availability('ktemplate-bla-bla-bla')
        True

    Returns:
        bool: if package name avaialbe return True otherwise False
    """
    url = f"https://pypi.org/pypi/{pkg_name}/json"
    response = get(url)
    return response.status_code != 200
