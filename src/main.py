"""Main executable entry points for the Microgrid Design Optimizer.

This module now exposes a small command-line interface so users can either run
the backend optimisation workflow or launch the Dash GUI using a single
command. The original orchestration logic lives in :func:`run_backend` and is
reused by the CLI entry point.
"""
from __future__ import annotations

import argparse

from core.emissions_mode import run_emissions_mode
from core.guarantee_loop import run_guarantee_loop
from core.layout_bos import evaluate_layout
from core.lcoe_mode import run_lcoe_mode
from core.montecarlo_validator import run_montecarlo_validation
from core.reliability_engine import ReliabilityEngine
from core.techno_economic import evaluate_technoeconomics
from utils.data_loader import load_inputs


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments for the optimiser launcher.

    Args:
        argv: Optional list of command-line arguments. If ``None``, arguments
            are pulled from :data:`sys.argv`.

    Returns:
        Parsed arguments describing the desired execution mode.
    """

    parser = argparse.ArgumentParser(description="Microgrid Design Optimizer")
    parser.add_argument(
        "--gui",
        action="store_true",
        help=(
            "Launch the Dash GUI instead of running the backend workflow. "
            "This is the primary command for interactive use."
        ),
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Host interface for the Dash server (only used with --gui).",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8050,
        help="Port for the Dash server (only used with --gui).",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Run the Dash server in debug mode (only used with --gui).",
    )
    return parser.parse_args(argv)


def run_backend() -> None:
    """Execute the optimisation workflow without starting the GUI."""

    config = load_inputs()
    mode_raw = config["preset"].get("mode")
    if not isinstance(mode_raw, str):
        raise ValueError("Preset 'mode' must be a string value.")

    mode = mode_raw.lower()
    config["preset"]["mode"] = mode

    if mode not in {"emissions", "lcoe"}:
        raise ValueError(f"Unsupported optimisation mode: {mode_raw}")

    re_engine = ReliabilityEngine()
    if mode == "emissions":
        results = run_emissions_mode(config, re_engine)
    else:
        results = run_lcoe_mode(config, re_engine)

    guaranteed = run_guarantee_loop(results, re_engine)
    economics = evaluate_technoeconomics(guaranteed)
    layout = evaluate_layout(economics)

    if config.get("run_validation", False):
        run_montecarlo_validation(layout, re_engine)

    print("✅ Optimisation completed. Results ready for GUI export.")


def run_gui(host: str, port: int, debug: bool) -> None:
    """Launch the Dash GUI server.

    Args:
        host: Host interface for the Dash development server.
        port: Port for the Dash development server.
        debug: Whether to run Dash in debug mode.
    """

    from gui_dash.app import app  # Imported lazily to avoid circular imports.

    print(
        "🚀 Starting Microgrid Design Optimizer GUI at "
        f"http://{host}:{port} (debug={'on' if debug else 'off'})"
    )
    app.run_server(host=host, port=port, debug=debug)


def main(argv: list[str] | None = None) -> None:
    """Command-line entry point for the optimiser and GUI launcher."""

    args = parse_args(argv)
    if args.gui:
        run_gui(args.host, args.port, args.debug)
    else:
        run_backend()


if __name__ == "__main__":
    main()
