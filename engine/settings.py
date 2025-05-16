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
    print(f"Registering setting \"{name}\" with default {default} ({type})")
    _defaults[name] = (type, default)


def get(name: str):
    """Gets a setting's value"""
    global _settings
    return _settings[name]


def init():
    """Loads or initializes the settings file, and gets the known settings"""

    global _defaults, _settings

    # try to load and parse the settings
    if path.exists(_SETTINGS_FILE):
        try:
            print(f"Loading settings from {_SETTINGS_FILE}")
            raw = None
            with open(_SETTINGS_FILE, "r") as f:
                raw = f.read()
            _settings = dict(json.loads(raw))
        except Exception as e:
            print(f"Failed to load settings from {_SETTINGS_FILE}: {e}")

    # if no settings were loaded, load defaults
    if not len(_settings):
        print(f"Loading default settings:\n{_defaults}")
        for k, (_, v) in _defaults.items():
            _settings[k] = v

    print(f"Got settings:\n{_settings}")


def save():
    """Saves the current settings to disk"""
    
    global _settings
    
    try:
        encoder = json.JSONEncoder()
        data = encoder.encode(_settings)
        print(f"Saving settings to {_SETTINGS_FILE}:\n{_settings}")
        with open(_SETTINGS_FILE, "w") as f:
            f.write(data)
    except Exception as e:
        print(f"Failed to save settings to {_SETTINGS_FILE}: {e}")
