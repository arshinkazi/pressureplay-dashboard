<div align="center">

# PressurePlay

**T20 cricket performance under pressure**  
A scouting analytics project for **SupeRR Selector Season 2, Round 1**

[Open the live dashboard](https://pressureplay-dashboard.streamlit.app/)

</div>

## About the project

PressurePlay looks at a question that overall career statistics do not always answer: which batters and bowlers perform well when the match situation gets difficult?

The project uses ball-by-ball IPL and T20 International data to build separate batting and bowling pressure rankings. It compares performance under pressure with each player's own non-pressure baseline, looks at consistency, and accounts for sample size.

## What you can explore

The Streamlit dashboard includes:

- Top-ten batting and bowling rankings
- Player search and minimum pressure-ball filters
- Individual player statistics and performance charts
- Side-by-side player comparisons
- Dataset overview and methodology

## Dataset

| Measure | Coverage |
|---|---:|
| Competitions in the supplied data pack | 141 |
| Matches in the supplied data pack | 883 |
| Ball-by-ball records in the supplied data pack | 200,999 |
| IPL and T20I matches analysed | 837 |
| Deliveries analysed | 193,988 |
| Batting pressure deliveries | 69,326 |
| Bowling pressure deliveries | 55,421 |
| Eligible players | 129 batters, 133 bowlers |

The analysis covers matches from 2022 to 1 November 2026. The leaderboards use the IPL and T20I matches in the supplied data pack.

## Key findings

- **Batting:** Fakhar Zaman leads the combined batting pressure ranking. Reeza Hendricks has the highest pressure average among the top ten, while Vaibhav Sooryavanshi has the highest pressure strike rate.
- **Bowling:** Sunil Narine leads the bowling ranking. Mitchell Santner is second, and Ravi Bishnoi has the largest pressure sample among the top five.
- **Rajasthan Royals:** Vaibhav Sooryavanshi and Ravi Bishnoi both appear in the top ten of their respective categories.

Sample size matters when reading these results. A strong rate from a smaller number of pressure deliveries should not be treated the same as a similar rate supported by a much larger sample.

## Method in brief

Pressure is defined using the match situation before each delivery. The analysis considers factors such as required run rate, wickets in hand, balls remaining and whether the innings is a chase. Batting and bowling have separate pressure definitions.

The ratings combine pressure performance, improvement over a player's non-pressure baseline and consistency. A second, more inclusive pressure definition is used as a sensitivity check. The final rankings use the average rank across the two definitions.

The core and relaxed rankings have Spearman correlations of 0.72 for batters and 0.71 for bowlers. Their top-ten overlap is 4 of 10 batters and 5 of 10 bowlers.

## Limitations

These rankings are intended as scouting evidence, not final selection or auction recommendations. Pressure is estimated from match state and is not a direct measure of a player's psychology. The analysis does not model player availability, fitness, auction price or squad role. Smaller samples should be interpreted with care.

## Research report

The [Round 1 research report](docs/SupeRR_Selector_Round1_Report.pdf) contains the detailed data preparation, methodology, results and limitations.

## Project post

I also shared the project and the process behind it on LinkedIn: [Read the PressurePlay post](ADD_LINKEDIN_POST_URL).

<!-- Replace ADD_LINKEDIN_POST_URL with the public LinkedIn post URL before publishing. -->

---

*Built as a student project exploring cricket, data and performance analysis.*
