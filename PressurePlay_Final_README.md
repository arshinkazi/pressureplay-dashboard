<div align="center">

# PressurePlay

### Reading the game when the game gets difficult.

**An interactive T20 pressure-performance scouting study**  
Built for **SupeRR Selector Season 2 · Round 1**

[**Explore the live dashboard ↗**](https://pressureplay-dashboard.streamlit.app/) · [View the quick rankings snapshot](https://arshinkazi.github.io/pressureplay-dashboard/) · [Read the research report](docs/SupeRR_Selector_Round1_Report.pdf) · [View the source code](https://github.com/arshinkazi/pressureplay-dashboard)

</div>

---

## The question behind the project

A player's overall numbers tell us what they have done. They do not always tell us what happens when the match tightens: the required rate climbs, wickets are down, the final overs arrive, or the opposition has room to attack.

**PressurePlay asks a more specific scouting question: which batters and bowlers continue to deliver when the match state becomes demanding?**

The project analyses ball-by-ball IPL and T20 International data, builds separate pressure-performance ratings for batting and bowling, and turns the results into an interactive scouting experience. Rather than treating reputation or aggregate career statistics as the answer, it compares each player's pressure output with their own non-pressure baseline, considers consistency across pressure innings, and accounts for the amount of evidence behind the numbers.

## Explore PressurePlay

<p align="center">
  <a href="https://pressureplay-dashboard.streamlit.app/"><strong>OPEN THE LIVE PRESSUREPLAY DASHBOARD →</strong></a>
</p>

The Streamlit dashboard is the primary experience. It is designed to move from the leaderboard to the underlying player evidence:

- **Overview** — the research at a glance, headline findings and leading players.
- **Batting rankings** — explore the top ten batters, search names, adjust the minimum pressure-ball threshold and inspect individual performance.
- **Bowling rankings** — examine pressure economy, bowling strike rate, wickets and consistency.
- **Player comparison** — compare two batters or two bowlers across the key pressure metrics.
- **Methodology** — see how pressure is defined, how the ratings are constructed and where the analysis has limits.

The dashboard is intended as a scouting aid: a way to interrogate the evidence, not just read a fixed list of names.

### Prefer the quick version?

The [Rankings Overview](https://arshinkazi.github.io/pressureplay-dashboard/) is a lightweight companion to the main dashboard. It presents the top-ten batting and bowling findings in a simple, direct format for readers who want to see the results at a glance. The Streamlit app remains the full interactive research experience; the HTML page is the quick snapshot.

## The analysis at a glance

| Coverage | Volume |
|---|---:|
| Supplied competitions | 141 |
| Matches in supplied data pack | 883 |
| Ball-by-ball records in supplied data pack | 200,999 |
| Selected IPL and T20I matches with ball data | **837** |
| Deliveries analysed in selected matches, innings 1 and 2 | **193,988** |
| Core-definition batting pressure deliveries | 69,326 |
| Core-definition bowling pressure deliveries | 55,421 |
| Eligible players in the core leaderboards | 129 batters · 133 bowlers |

**Data window:** 2022 to 1 November 2026. The analysis uses IPL and T20 International matches from the supplied SupeRR Selector data pack. Other T20 competitions in the pack were not included in the leaderboards.

## What emerged

### Batting

**Fakhar Zaman** leads the combined batting pressure ranking. **Reeza Hendricks** records the highest pressure average among the top ten (55.6), while **Vaibhav Sooryavanshi** has the highest pressure strike rate in the list (236.3).

Sample size changes how these numbers should be read. Tim David has 646 pressure balls across 44 pressure innings among the top three, compared with Fakhar Zaman's 146 balls across 11 innings. Sooryavanshi's strike rate is striking, but his 113-ball sample sits close to the minimum eligibility threshold.

### Bowling

**Sunil Narine** leads the bowling ranking, with a pressure economy of 7.44 and 24 wickets from 462 pressure balls. **Mitchell Santner** ranks second, taking 37 wickets from 443 pressure balls. **Ravi Bishnoi** has the largest pressure sample among the top five: 901 balls and 53 wickets.

The project reads economy alongside bowling strike rate and consistency. A wicket-taking rate on its own does not capture the cost of those wickets or the runs conceded under pressure.

### What this could mean for Rajasthan Royals

The analysis places **Vaibhav Sooryavanshi** and **Ravi Bishnoi** in the top ten of their respective disciplines. That is a useful signal for role planning and player development within the squad. It is not, by itself, a recruitment recommendation: auction registration, availability, role fit, fitness, squad balance and price need separate assessment.

## How pressure is defined

Pressure is treated as a **match state, not simply the final overs**. Each delivery is labelled using the state immediately before it, so the outcome of the delivery cannot determine its own pressure label.

The model considers factors including:

- Required run rate and the gap between required and current scoring rates.
- Wickets in hand.
- Legal balls remaining and innings stage.
- Whether the innings is a first-innings setting or a chase.

Batting and bowling use separate core definitions because the same match situation can create different demands for the two roles. For example, a batter may be under pressure when the chase rate rises sharply or wickets fall; a bowler may be under pressure when the opposition is scoring quickly with wickets available.

A second, more inclusive **relaxed pressure definition** is used as a sensitivity check. The final leaderboard order is based on the average rank under the core and relaxed definitions, rather than relying on one set of cut-offs alone.

## How the ratings are built

### Batting indicators

- **Pressure strike rate** — pressure runs per 100 legal balls.
- **Pressure average** — pressure runs per dismissal.
- **Strike-rate uplift** — pressure strike rate minus the player's non-pressure strike rate.
- **Consistency** — share of pressure innings in which the player's pressure strike rate meets or exceeds their own non-pressure baseline.

### Bowling indicators

- **Pressure economy** — runs conceded per six legal balls under pressure.
- **Pressure bowling strike rate** — legal pressure balls per bowler-credited wicket.
- **Economy improvement** — non-pressure economy minus pressure economy.
- **Consistency** — share of pressure innings in which the player's pressure economy is no higher than their own non-pressure baseline.

### Composite score and eligibility

Each component is winsorised at the 2nd and 98th percentiles and standardised within format-season groups. The season-level composite uses these weights:

| Discipline | Component | Weight |
|---|---|---:|
| Batting | Pressure strike rate | 35% |
| Batting | Pressure average | 25% |
| Batting | Strike-rate uplift | 20% |
| Batting | Pressure-innings consistency | 20% |
| Bowling | Pressure economy | 35% |
| Bowling | Bowling strike rate | 25% |
| Bowling | Economy improvement | 20% |
| Bowling | Pressure-innings consistency | 20% |

Format-season scores are combined using the square root of pressure-ball volume as the weight. A reliability factor, `√[n / (n + 150)]`, then reduces the influence of smaller pressure samples. Players need at least **100 pressure legal balls** and **eight pressure innings** to qualify; a pressure innings must contain at least six legal pressure balls. Eligibility is assessed separately under the core and relaxed definitions.

## Robustness and interpretation

The core and relaxed definitions produce related, but not identical, rankings:

| Sensitivity check | Batters | Bowlers |
|---|---:|---:|
| Spearman rank correlation | 0.72 | 0.71 |
| Top-ten membership overlap | 4 of 10 | 5 of 10 |

The correlations suggest that the broad ordering is related across the two definitions. The overlap also makes clear that top-ten membership is sensitive to the pressure thresholds for some players. Averaging ranks reduces dependence on one definition; it does not eliminate uncertainty.

### Important limitations

- Pressure is a transparent proxy built from recorded match state, not a direct measurement of a player's psychology.
- IPL and T20I conditions differ, even after format-season standardisation.
- Smaller pressure samples provide less evidence and should be interpreted cautiously.
- The composite is a comparative index within this dataset, not a probability of future success or a forecast of a player's next season.
- Auction registration, availability, expected price, fitness and role are not modelled.
- The analysis ends on **1 November 2026** and does not include later matches.

For those reasons, PressurePlay should be used to identify players and patterns worth investigating further—not as a standalone selection or bidding model.

## Research report

The accompanying [SupeRR Selector Round 1 report](docs/SupeRR_Selector_Round1_Report.pdf) documents the research question, data preparation, pressure definitions, scoring methodology, leaderboards, implications for Rajasthan Royals, sensitivity checks and limitations.

---

## Project story

PressurePlay was also shared on LinkedIn as part of the SupeRR Selector Season 2 journey. The post captures the motivation behind the project, the process of turning ball-by-ball cricket data into a pressure-performance study, and the experience of building the interactive dashboard.

**[Read the PressurePlay project post on LinkedIn](ADD_LINKEDIN_POST_URL)**

<!-- Replace ADD_LINKEDIN_POST_URL with the public permalink to the LinkedIn post before publishing this README. -->

---

<div align="center">

**PressurePlay**  
*Performance under pressure, made explorable.*

[Live dashboard](https://pressureplay-dashboard.streamlit.app/) · [Rankings Overview](https://arshinkazi.github.io/pressureplay-dashboard/) · [Research report](docs/SupeRR_Selector_Round1_Report.pdf) · [GitHub repository](https://github.com/arshinkazi/pressureplay-dashboard)

</div>
