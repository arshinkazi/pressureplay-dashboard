# PressurePlay

**An interactive T20 pressure-performance scouting dashboard** created for **SupeRR Selector Season 2, Round 1**.

## Live demos

- **Primary dashboard — Streamlit:** https://pressureplay-dashboard.streamlit.app/
- **HTML companion — GitHub Pages:** https://arshinkazi.github.io/pressureplay-dashboard/
- **Source code:** https://github.com/arshinkazi/pressureplay-dashboard

The Streamlit app is the primary analytical experience, with player search, filters, player inspection, comparisons and methodology. The HTML dashboard is a lightweight companion for quickly exploring the presented findings.

## What the project explores

PressurePlay examines player performance in demanding T20 match situations, with separate batting and bowling views. It brings together pressure-specific performance indicators, consistency and sample-size context to support a more informed scouting discussion.

### Dashboard features

- Separate batting and bowling rankings
- Player search and minimum pressure-ball filters
- Individual player performance inspection
- Side-by-side player comparisons
- Summary charts and dataset coverage indicators
- Methodology, scoring weights, definitions and limitations

## Run locally

Python 3.10 or newer is recommended.

```bash
python -m venv .venv
```

Activate the environment:

```bash
# Windows
.venv\\Scripts\\activate

# macOS / Linux
source .venv/bin/activate
```

Install dependencies and launch:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy the Streamlit app

1. Push the repository to GitHub.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/).
3. Sign in with GitHub and grant access to this repository.
4. Create a new app using this repository, the `main` branch and `app.py` as the main file.
5. Deploy. Streamlit installs the dependencies listed in `requirements.txt`.

## Deploy the HTML companion

The `index.html` file is a standalone HTML dashboard and can be hosted through GitHub Pages:

1. Open the repository's **Settings → Pages**.
2. Choose **Deploy from a branch**.
3. Select `main` and the root folder (`/`).
4. Save and wait for the Pages deployment.

## Project structure

```text
pressureplay-dashboard/
├── app.py
├── index.html
├── rankings.csv
├── requirements.txt
├── render.yaml
├── README.md
├── DEPLOY.md
├── .streamlit/
│   └── config.toml
└── docs/
    └── SupeRR_Selector_Round1_Report.pdf
```

## Data, methodology and limitations

The dashboard uses derived player-level summary metrics from the supplied competition data pack. It does not publish the raw ball-by-ball dataset. Check the competition's data-use and sharing terms before distributing derived results.

The analysis covers IPL and T20 International matches in the supplied data window (2022 to 1 November 2026). The dashboard's Methodology section describes the pressure definitions, batting and bowling measures, scoring weights, sample-size adjustment and eligibility thresholds.

These rankings are statistical scouting evidence, not definitive recruitment recommendations. Auction registration, availability, price, fitness and role are not modelled. Pressure is a match-state proxy and should not be interpreted as a direct measure of a player's psychology.

## Submission report

The Round 1 report is included in `docs/`. The live dashboards should be used alongside the report to understand the findings and the methodology behind them.
