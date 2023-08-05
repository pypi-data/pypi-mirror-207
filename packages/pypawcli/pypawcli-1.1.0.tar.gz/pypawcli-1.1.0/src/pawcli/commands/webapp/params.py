from typer import Argument
from typer import Option

from pawcli.core.path import resolve

DOMAIN_ARGUMENT = Argument(
    ...,
    metavar="DOMAIN",
    help="App domain name",
)
DOMAIN_OPTION = Option(
    ...,
    "--domain",
    "-d",
    metavar="DOMAIN",
    help="App domain name",
)
PYTHON_VERSION_OPTION = Option(
    None,
    "--py",
    help="Python version",
)

APP_SRC_OPTION = Option(
    None,
    metavar="PATH",
    help="Source directory",
)
APP_VENV_OPTION = Option(
    None,
    metavar="PATH",
    help="Virtualenv path",
)
APP_HTTPS_OPTION = Option(
    None,
    "--https/--http",
    is_flag=True,
    help="Enbale/Disable force HTTPS",
)
APP_PROTECTION_OPTION = Option(
    None,
    "--priv/--pub",
    is_flag=True,
    help="Enable/Disable password protection",
)
APP_PROTECTION_USERNAME_OPTION = Option(
    None,
    "--username",
    "-u",
    help="Username for password protection",
)
APP_PROTECTION_PASSWORD_OPTION = Option(
    None,
    "--password",
    "-p",
    help="Password for password protection",
)

HEADER_ID_ARGUMENT = Argument(
    ...,
    metavar="ID",
    help="Header ID",
)
HEADER_URL_OPTION = Option(
    ...,
    "--url",
    "-u",
    metavar="URL",
    help="Header URL",
)
HEADER_NAME_OPTION = Option(
    ...,
    "--name",
    "-n",
    metavar="NAME",
    help="Header name",
)
HEADER_VALUE_OPTION = Option(
    ...,
    "--value",
    "-v",
    metavar="VALUE",
    help="Header value",
)

FILE_ID_ARGUMENT = Argument(
    ...,
    metavar="ID",
    help="Static file ID",
)
FILES_URL_OPTION = Option(
    ...,
    "--url",
    "-u",
    metavar="URL",
    help="URL for static files",
)
FILES_PATH_OPTION = Option(
    ...,
    "--path",
    "-p",
    callback=resolve,
    metavar="PATH",
    help="Directory with static files",
)
