"""Utility helpers for loading configuration inputs."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from utils.logger import get_logger

LOGGER = get_logger(__name__)

# Derive the repository's ``src`` directory so JSON assets can be located
# regardless of the current working directory. This avoids ``FileNotFoundError``
# when the package is executed from outside the project root.
SRC_DIR = Path(__file__).resolve().parents[1]
CONFIG_DIR = SRC_DIR / "config"

CONFIG_FILES = {
    "preset": CONFIG_DIR / "presets.json",
    "tech": CONFIG_DIR / "tech_data.json",
    "financial": CONFIG_DIR / "financial_scenarios.json",
    "site": CONFIG_DIR / "site_data.json",
}


def _load_json(path: Path) -> Dict[str, Any]:
    """Load a JSON file and return its contents."""

    try:
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError as exc:  # pragma: no cover - defensive programming
        LOGGER.error("Configuration file missing: %s", path)
        raise ValueError(f"Missing configuration file: {path}") from exc


def load_inputs() -> Dict[str, Any]:
    """Load default configuration inputs from JSON files.

    Returns:
        A dictionary consolidating presets, technology data, financial
        scenarios, and site information. The preset file may also define the
        ``run_validation`` flag, which is hoisted to the top level for
        convenience.

    Raises:
        ValueError: If the preset file does not contain a mode selection.
    """

    config: Dict[str, Any] = {}
    for key, path in CONFIG_FILES.items():
        LOGGER.debug("Loading configuration '%s' from %s", key, path)
        data = _load_json(path)

        if key == "preset":
            preset_data = data.get("preset", {})
            if "mode" not in preset_data:
                raise ValueError(
                    "Preset configuration must define a 'mode' value."
                )
            config["preset"] = preset_data
            if "run_validation" in data:
                config["run_validation"] = bool(data["run_validation"])
        else:
            config[key] = data

    config.setdefault("run_validation", False)
    return config
