import argparse
import pathlib
import sys
from dataclasses import dataclass, field
from typing import Any


@dataclass
class VerificationResult:
    file_path: pathlib.Path
    errors: dict[str, bool] = field(default_factory=dict)


def get_file_list(path_raw: str, file_name: str = "router.db") -> list[pathlib.Path]:
    """Get files from provided path."""

    path = pathlib.Path(path_raw)

    if path.is_file():
        return [path]

    return list(path.glob(file_name))


def verify_file(file_path: str | pathlib.Path) -> Any:
    file_path = pathlib.Path(file_path)
    result = VerificationResult(file_path=pathlib.Path(file_path))

    if not file_path.exists():
        result.errors["not_found"] = True
        return result

    try:
        open(file_path, "r", encoding="utf-8").read()
    except UnicodeDecodeError:
        result.errors["not_utf8"] = True

    return result


def print_results(results: list[VerificationResult]) -> None:
    for result in results:
        if len(result.errors) == 0:
            status: str = "OK"
        else:
            status: str = "Error"
        print(f"{str(result.file_path)} {status}")


def parse_args() -> argparse.Namespace:
    parser: argparse.ArgumentParser = argparse.ArgumentParser()

    parser.add_argument("path", help="Folder to look for router.db in")
    parser.add_argument(
        "-q", "--quite", action="store_true", help="Dont print anything"
    )

    return parser.parse_args()


def cli() -> None:
    args: argparse.Namespace = parse_args()

    results: list[VerificationResult] = []

    exit_code: int = 0

    for file_path in get_file_list(args.path):
        result: VerificationResult = verify_file(file_path)
        if len(result.errors) > 0:
            exit_code = 1
        results.append(result)

    if args.quite:
        sys.exit(exit_code)

    print_results(results)

    sys.exit(exit_code)
