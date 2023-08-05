import os
import sys

from pawapi.exceptions import PythonAnywhereAPIException

if not __package__:
    pawcli_package_source = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, pawcli_package_source)

from pawcli.app import app
from pawcli.core.config import APP_NAME


def run() -> int:
    try:
        app(prog_name=APP_NAME)
    except PythonAnywhereAPIException as error:
        description = f"Request failed with status {error.status_code}"
        if error.description is not None:
            description = f"{error.description} (status={error.status_code})"
        print(description)
    except Exception as error:
        print(error)
    else:
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(run())
