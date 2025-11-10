"""Utility helpers for loading configuration inputs."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from utils.logger import get_logger

LOGGER = get_logger(__name__)

CONFIG_FILES = {
    "preset": "src/config/presets.json",
    "tech": "src/config/tech_data.json",
    "financial": "src/config/financial_scenarios.json",
    "site": "src/config/site_data.json",
}


def load_inputs() -> Dict[str, Any]:
    """Load default configuration inputs from JSON files."""
    config: Dict[str, Any] = {}
    for key, relative_path in CONFIG_FILES.items():
        path = Path(relative_path)
        LOGGER.debug("Loading configuration '%s' from %s", key, path)
        with path.open(encoding="utf-8") as handle:
            config[key] = json.load(handle)
    return config
