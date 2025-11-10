"""
Main orchestrator for Microgrid Design Optimizer.
Selects optimisation mode, runs reliability checks, and dispatches outputs.
"""
from core.emissions_mode import run_emissions_mode
from core.lcoe_mode import run_lcoe_mode
from core.reliability_engine import ReliabilityEngine
from core.guarantee_loop import run_guarantee_loop
from core.techno_economic import evaluate_technoeconomics
from core.layout_bos import evaluate_layout
from core.montecarlo_validator import run_montecarlo_validation
from utils.data_loader import load_inputs


def main() -> None:
    """Entry point for orchestrating the microgrid optimisation workflow."""
    config = load_inputs()
    mode = config["preset"]["mode"]

    re = ReliabilityEngine()
    if mode == "emissions":
        results = run_emissions_mode(config, re)
    else:
        results = run_lcoe_mode(config, re)

    guaranteed = run_guarantee_loop(results, re)
    economics = evaluate_technoeconomics(guaranteed)
    layout = evaluate_layout(economics)

    if config.get("run_validation", False):
        run_montecarlo_validation(layout, re)

    print("✅ Optimisation completed. Results ready for GUI export.")


if __name__ == "__main__":
    main()
