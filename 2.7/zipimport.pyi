"""Stub file for the 'zipimport' module."""
# This is an autogenerated file. It serves as a starting point
# for a more precise manual annotation of this module.
# Feel free to edit the source below, but remove this header when you do.

from typing import Any, List, Tuple, Dict, GenericType

class zipimporter(object):
    def find_module(a: str, *args, **kwargs) -> None: ...
    def get_code(a: str) -> Any: ...
    def get_data(a: str) -> str:
        raise IOError()
    def get_filename(a: str) -> str: ...
    def get_source(a: str) -> Any: ...
    def is_package(a: str) -> bool: ...
    def load_module(a: str) -> Any: ...