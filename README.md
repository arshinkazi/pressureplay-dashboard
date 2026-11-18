# PressurePlay

**Interactive T20 pressure-performance scouting dashboard** built for SupeRR Selector Season 2, Round 1.

## Live demos

- **Streamlit analytical dashboard (primary):** _Add your deployed Streamlit URL here_
- **HTML dashboard (GitHub Pages):** _Add your published GitHub Pages URL here_
- **Source code:** This GitHub repository

The Streamlit app is the primary analytical experience. The HTML version is a lightweight companion that can be opened without a Python server.

## What it includes

- Separate batting and bowling pressure rankings
- Player search and minimum pressure-ball filters
- Player-level performance inspection
- Side-by-side player comparisons
- Summary charts and dataset coverage indicators
- Plain-language methodology, scoring weights and limitations

## Run locally

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Push this repository to GitHub.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/).
3. Sign in with GitHub and authorize access to this repository.
4. Choose **Create app**.
5. Select this repository, branch `main`, and main file path `app.py`.
6. Deploy. Streamlit will install packages from `requirements.txt`.

## Project contents

- `app.py` — Streamlit application
- `index.html` — standalone HTML dashboard for GitHub Pages
- `rankings.csv` — derived top-ten batter and bowler summary metrics
- `requirements.txt` — Python dependencies
- `docs/` — submission report (add the final PDF here)

## Data and interpretation notes

The dashboard contains derived player-level summary metrics from the competition data pack. It does not include the raw ball-by-ball file. Check the competition's data-use and sharing terms before publishing or distributing derived results.

Rankings are statistical pressure rankings, not auction recommendations. The dashboard does not model auction registration, availability, price, fitness or role. Pressure is a match-state proxy and should not be interpreted as a direct measure of a player's psychology.

## Method summary

The analysis uses IPL and T20 International matches in the supplied data window (2022 to 1 November 2026). The dashboard explains the pressure definitions, batting and bowling measures, scoring weights, sample-size adjustment and eligibility thresholds in its Methodology section.
