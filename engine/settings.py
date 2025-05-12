"""This module implements a rudimentary settings file"""

import json
import os

from os import path
from typing import Any, Type

_SETTINGS_FILE = "settings.json"

_defaults: dict[str, tuple[Type, Any]] = {}

_settings: dict[str, Any] = {}

def add(name: str, default, type: Type | None):
    """Registers a setting"""
    global _defaults
    _defaults[name] = (type, default)


def init():
    """Loads or initializes the settings file, and gets the known settings"""

    global _defaults, _settings

    # try to load and parse the settings
    if path.exists(_SETTINGS_FILE):
        try:
            print(f"Loading settings in {_SETTINGS_FILE}")
            raw = None
            with open(_SETTINGS_FILE, "r") as f:
                raw = f.read()
            _settings = dict(json.loads(raw))
        except Exception as e:
            print(f"Failed to load settings in {_SETTINGS_FILE}: {e}")

    # if no settings were loaded, load defaults
    if _settings is None:
        print(f"Loading default settings:\n{_defaults}")
        for k, (_, default) in _defaults:
            _settings[k] = default
