# PressurePlay

A lightweight T20 cricket scouting dashboard built for SupeRR Selector Season 2, Round 1.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Project contents

- `app.py` — Streamlit dashboard
- `rankings.csv` — top-ten batter and bowler summary metrics used by the dashboard
- `requirements.txt` — Python dependencies

## Data note

The dashboard contains derived player-level summary metrics from the competition data pack. It does not include the raw ball-by-ball file. Check the competition's data-use and sharing terms before publishing or distributing any derived results. If public sharing is not permitted, deploy privately or replace the CSV with permitted public data.

## Method

The dashboard presents the two ranked lists, player-level summary metrics, comparisons and a plain-language explanation of the pressure methodology. It is a scouting aid, not an auction availability or price model.
