# Microgrid Design Optimizer (Dash Edition)

Python-based tool for designing and optimising modular microgrids (CHP + PV + BESS) for data-centre and industrial applications.

## Key Features
- Emissions- and LCOE-optimised modes
- Firm-power and reliability guarantees
- Central reliability engine and guarantee loop
- Techno-economic & BOS evaluation
- Monte-Carlo validation
- Interactive Dash web GUI

## Quick Start
```
pip install -r requirements.txt
python src/gui_dash/app.py
```

To run the console-only optimisation workflow, execute `python src/main.py`. If
you prefer launching the Dash GUI through the CLI entry point instead of the
module above, use `python src/main.py --gui`.

## Folder Structure
```
microgrid-design-optimizer/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── main.py
│   ├── __init__.py
│   ├── config/
│   │   ├── presets.json
│   │   ├── tech_data.json
│   │   ├── financial_scenarios.json
│   │   └── site_data.json
│   ├── core/
│   │   ├── emissions_mode.py
│   │   ├── lcoe_mode.py
│   │   ├── reliability_engine.py
│   │   ├── guarantee_loop.py
│   │   ├── techno_economic.py
│   │   ├── layout_bos.py
│   │   ├── dispatch_simulator.py
│   │   └── montecarlo_validator.py
│   ├── gui_dash/
│   │   ├── app.py
│   │   ├── callbacks.py
│   │   ├── layouts/
│   │   │   ├── layout_inputs.py
│   │   │   ├── layout_results.py
│   │   │   └── layout_validation.py
│   │   └── assets/
│   │       ├── styles.css
│   │       └── logo.png
│   ├── utils/
│   │   ├── data_loader.py
│   │   ├── logger.py
│   │   ├── visualizer.py
│   │   └── validators.py
│   └── tests/
│       ├── test_reliability.py
│       ├── test_modes.py
│       └── test_layout.py
└── notebooks/
    ├── development_notes.ipynb
    └── validation_experiments.ipynb
```

## License
MIT
