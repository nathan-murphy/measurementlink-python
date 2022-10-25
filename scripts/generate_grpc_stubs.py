#!/usr/bin/env python3
"""Generates gRPC Python stubs from proto files."""

import itertools
import pathlib

import black
import grpc_tools.protoc
import pkg_resources
from black.mode import Mode


STUBS_NAMESPACE = "ni_measurement_service._internal.stubs"
STUBS_PATH = pathlib.Path(__file__).parent.parent / STUBS_NAMESPACE.replace(".", "/")
PROTO_PATH = STUBS_PATH / "proto"
PROTO_FILES = list(PROTO_PATH.rglob("*.proto"))


def main():
    """Generate and fixup gRPC Python stubs."""
    remove_generated_files()
    generate_python_files()
    fix_import_paths()
    blacken_code()


def remove_generated_files():
    """Remove files generated by protoc."""
    for path in itertools.chain(STUBS_PATH.rglob("*pb2*py"), STUBS_PATH.rglob("*.pyi")):
        path.unlink()


def generate_python_files():
    """Generate python files from .proto files with protoc."""
    arguments = [
        "protoc",
        f"--proto_path={str(PROTO_PATH)}",
        f"--proto_path={pkg_resources.resource_filename('grpc_tools', '_proto')}",
        f"--python_out={str(STUBS_PATH)}",
        f"--mypy_out={str(STUBS_PATH)}",
        f"--grpc_python_out={str(STUBS_PATH)}",
    ]
    arguments += [str(path.relative_to(PROTO_PATH)).replace("\\", "/") for path in PROTO_FILES]

    grpc_tools.protoc.main(arguments)


def fix_import_paths():
    """Fix import paths of generated files."""
    print("Fixing import paths")
    grpc_codegened_file_paths = list(STUBS_PATH.rglob("*pb2*py"))
    imports_to_fix = [path.stem for path in grpc_codegened_file_paths if path.parent == STUBS_PATH]
    for path in grpc_codegened_file_paths:
        print(f"Processing {path}")
        data = path.read_bytes()
        if path.parent == STUBS_PATH:
            for name in imports_to_fix:
                data = data.replace(
                    f"import {name}".encode(), f"from {STUBS_NAMESPACE} import {name}".encode()
                )

        data = data.replace(
            "from ni.measurements".encode(), f"from {STUBS_NAMESPACE}.ni.measurements".encode()
        )
        path.write_bytes(data)


def blacken_code():
    """Run black on generated files."""
    print("Running black")
    for py_path in itertools.chain(STUBS_PATH.rglob("*.py"), STUBS_PATH.rglob("*.pyi")):
        if black.format_file_in_place(
            src=py_path, fast=False, mode=Mode(line_length=100), write_back=black.WriteBack.YES
        ):
            print(f"reformatted {py_path}")


if __name__ == "__main__":
    main()
