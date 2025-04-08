from subprocess import check_call


def start() -> None:
    check_call(["python", "-m", "src"])


def test() -> None:
    check_call(["pytest", "tests"])


def lint() -> None:
    check_call(["ruff", "check"])


def format() -> None:
    check_call(["ruff", "format"])
