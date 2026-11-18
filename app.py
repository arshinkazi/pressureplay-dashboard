import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="PressurePlay | T20 scouting notes", page_icon="🏏", layout="wide")

PAPER = "#f7f5ef"
INK = "#252b27"
MUTED = "#69716b"
GREEN = "#355b45"
RUST = "#a34f38"
LINE = "#deded5"

st.markdown(f"""
<style>
    .stApp {{ background: {PAPER}; color: {INK}; }}
    section[data-testid="stSidebar"] {{ background: #eeede6; border-right: 1px solid {LINE}; }}
    h1, h2, h3 {{ font-family: Georgia, 'Times New Roman', serif !important; color: {INK}; }}
    p, label, div {{ font-family: Arial, Helvetica, sans-serif; }}
    .eyebrow {{ color: {GREEN}; font-size: 11px; letter-spacing: 1.8px; text-transform: uppercase; }}
    .deck {{ color: {MUTED}; font-family: Georgia, serif; font-size: 17px; line-height: 1.45; }}
    .rule {{ border-top: 1px solid {LINE}; margin: 14px 0 20px 0; }}
    .stat {{ border-top: 2px solid {GREEN}; padding: 10px 0 6px 0; }}
    .stat .num {{ font-family: Georgia, serif; font-size: 28px; color: {INK}; }}
    .stat .lbl {{ font-size: 11px; color: {MUTED}; text-transform: uppercase; letter-spacing: .8px; }}
    .note {{ background: #efeee8; border-left: 3px solid {RUST}; padding: 10px 13px; color: {INK}; }}
    .small {{ font-size: 12px; color: {MUTED}; }}
    [data-testid="stDataFrame"] {{ border: 1px solid {LINE}; }}
    div[data-testid="stMetric"] {{ background: transparent; border-top: 2px solid {GREEN}; padding-top: 9px; }}
    .stButton button {{ border-radius: 3px; border: 1px solid {GREEN}; color: {GREEN}; background: transparent; }}
</style>
""", unsafe_allow_html=True)

df = pd.read_csv("rankings.csv")
bat = df[df.category == "Batter"].sort_values("rank").copy()
bowl = df[df.category == "Bowler"].sort_values("rank").copy()

st.markdown('<div class="eyebrow">SupeRR Selector Season 2 · Round 1</div>', unsafe_allow_html=True)
st.title("PressurePlay")
st.markdown('<div class="deck">A small scouting notebook on who holds their shape when a T20 innings gets difficult.</div>', unsafe_allow_html=True)
st.markdown('<div class="rule"></div>', unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### Match room")
    section = st.radio("Go to", ["Overview", "Batters", "Bowlers", "Player comparison", "How this was measured"])
    st.markdown("---")
    st.caption("Data window: 2022 to 1 November 2026")
    st.caption("Competitions: IPL and T20 Internationals")
    st.caption("Source: supplied SupeRR Selector data pack")

if section == "Overview":
    c1,c2,c3,c4 = st.columns(4)
    for col, value, label in [
        (c1,"837","matches in scope"),
        (c2,"193,988","deliveries analysed"),
        (c3,"69,326","batter-pressure balls"),
        (c4,"55,421","bowler-pressure balls"),
    ]:
        with col:
            st.markdown(f'<div class="stat"><div class="num">{value}</div><div class="lbl">{label}</div></div>',unsafe_allow_html=True)

    st.markdown("## The short read")
    left,right=st.columns([1.15,1])
    with left:
        st.markdown("**Batting**")
        st.write("Fakhar Zaman leads the combined pressure ranking. Tim David has the largest pressure-ball sample among the top three, while Vaibhav Sooryavanshi posts the highest pressure strike rate in the top ten.")
        st.markdown("**Bowling**")
        st.write("Sunil Narine leads the bowling list. Ravi Bishnoi has the largest pressure sample among the top five, which gives his results a broader evidence base.")
    with right:
        st.markdown('<div class="note"><b>A note on reading the ranks</b><br>These are statistical pressure rankings, not auction availability recommendations. Sample size, role, registration and price still matter.</div>',unsafe_allow_html=True)
    st.markdown("## At a glance")
    a,b=st.columns(2)
    with a:
        st.markdown("**Top batting scores**")
        fig=px.bar(bat.sort_values("pressure_strike_rate"),x="pressure_strike_rate",y="player",orientation="h",
                   labels={"pressure_strike_rate":"Pressure strike rate","player":""})
        fig.update_traces(marker_color=GREEN)
        fig.update_layout(height=390,margin=dict(l=0,r=10,t=10,b=10),paper_bgcolor=PAPER,plot_bgcolor=PAPER,
                          font=dict(color=INK),xaxis=dict(showgrid=True,gridcolor=LINE),yaxis=dict(showgrid=False))
        st.plotly_chart(fig,use_container_width=True)
    with b:
        st.markdown("**Top bowling economy**")
        fig=px.bar(bowl.sort_values("pressure_economy",ascending=False),x="pressure_economy",y="player",orientation="h",
                   labels={"pressure_economy":"Pressure economy","player":""})
        fig.update_traces(marker_color=RUST)
        fig.update_layout(height=390,margin=dict(l=0,r=10,t=10,b=10),paper_bgcolor=PAPER,plot_bgcolor=PAPER,
                          font=dict(color=INK),xaxis=dict(showgrid=True,gridcolor=LINE),yaxis=dict(showgrid=False))
        st.plotly_chart(fig,use_container_width=True)

elif section == "Batters":
    st.markdown("## Batters under pressure")
    st.caption("Rank order uses the average position under the core and relaxed pressure definitions. Table values are from the core definition.")
    show=bat[["rank","player","pressure_balls","pressure_innings","pressure_runs","pressure_strike_rate","pressure_average","pressure_innings_success_rate"]].rename(columns={
        "rank":"Rank","player":"Player","pressure_balls":"Balls","pressure_innings":"Innings","pressure_runs":"Runs",
        "pressure_strike_rate":"Pressure SR","pressure_average":"Pressure average","pressure_innings_success_rate":"Innings consistency (%)"})
    st.dataframe(show,hide_index=True,use_container_width=True)
    chosen=st.selectbox("Inspect a batter",bat.player.tolist())
    r=bat[bat.player==chosen].iloc[0]
    x1,x2,x3,x4=st.columns(4)
    x1.metric("Pressure strike rate",f"{r.pressure_strike_rate:.1f}")
    x2.metric("Pressure average",f"{r.pressure_average:.1f}")
    x3.metric("Pressure balls",int(r.pressure_balls))
    x4.metric("Innings consistency",f"{r.pressure_innings_success_rate:.1f}%")
    st.markdown(f"**Scouting note:** {chosen} recorded {int(r.pressure_runs)} runs from {int(r.pressure_balls)} pressure balls across {int(r.pressure_innings)} pressure innings in the analysis sample.")

elif section == "Bowlers":
    st.markdown("## Bowlers under pressure")
    st.caption("Lower pressure economy and bowling strike rate indicate better run control and wicket frequency.")
    show=bowl[["rank","player","pressure_balls","pressure_innings","pressure_wickets","pressure_economy","pressure_bowling_strike_rate","pressure_innings_success_rate"]].rename(columns={
        "rank":"Rank","player":"Player","pressure_balls":"Balls","pressure_innings":"Innings","pressure_wickets":"Wickets",
        "pressure_economy":"Pressure economy","pressure_bowling_strike_rate":"Bowling strike rate","pressure_innings_success_rate":"Innings consistency (%)"})
    st.dataframe(show,hide_index=True,use_container_width=True)
    chosen=st.selectbox("Inspect a bowler",bowl.player.tolist())
    r=bowl[bowl.player==chosen].iloc[0]
    x1,x2,x3,x4=st.columns(4)
    x1.metric("Pressure economy",f"{r.pressure_economy:.2f}")
    x2.metric("Bowling strike rate",f"{r.pressure_bowling_strike_rate:.2f}")
    x3.metric("Pressure wickets",int(r.pressure_wickets))
    x4.metric("Innings consistency",f"{r.pressure_innings_success_rate:.1f}%")
    st.markdown(f"**Scouting note:** {chosen} took {int(r.pressure_wickets)} wickets from {int(r.pressure_balls)} pressure balls across {int(r.pressure_innings)} pressure innings.")

elif section == "Player comparison":
    st.markdown("## Compare players")
    kind=st.radio("Discipline",["Batters","Bowlers"],horizontal=True)
    source=bat if kind=="Batters" else bowl
    options=source.player.tolist()
    p1,p2=st.columns(2)
    with p1: one=st.selectbox("Player one",options,index=0)
    with p2: two=st.selectbox("Player two",options,index=min(1,len(options)-1))
    comp=source[source.player.isin([one,two])].copy()
    if kind=="Batters":
        cols=["pressure_strike_rate","pressure_average","pressure_innings_success_rate","pressure_balls"]
        labels=["Pressure strike rate","Pressure average","Consistency (%)","Pressure balls"]
    else:
        cols=["pressure_economy","pressure_bowling_strike_rate","pressure_innings_success_rate","pressure_balls"]
        labels=["Pressure economy","Bowling strike rate","Consistency (%)","Pressure balls"]
    for col,label in zip(cols,labels):
        st.markdown(f"**{label}**")
        st.dataframe(comp[["player",col]].rename(columns={"player":"Player",col:label}),hide_index=True,use_container_width=True)

else:
    st.markdown("## How the rankings were built")
    st.markdown("""
**Pressure is a match state, not simply the final overs.** The analysis labels pressure before each delivery, using the chase rate, current rate, wickets in hand, balls remaining and innings stage. Batting and bowling have separate rules.

**Batting measures**
- Pressure strike rate and pressure average
- Strike-rate uplift against the player's non-pressure baseline
- Share of pressure innings at or above the player's own baseline strike rate

**Bowling measures**
- Pressure economy and bowling strike rate
- Economy improvement against the player's non-pressure baseline
- Share of pressure innings at or below the player's own baseline economy

**Scoring**
- Components are winsorised at the 2nd and 98th percentiles and standardised within format-season groups.
- Batting weights: 35% pressure strike rate, 25% pressure average, 20% uplift and 20% consistency.
- Bowling weights: 35% pressure economy, 25% bowling strike rate, 20% economy improvement and 20% consistency.
- A sample-size adjustment shrinks scores with fewer pressure balls.
- Final order is the average rank across core and relaxed pressure definitions.

**Scope and limits**
- IPL and T20 Internationals, 2022 to 1 November 2026.
- At least 100 pressure balls and eight pressure innings for eligibility.
- Pressure is a proxy based on match state, not a direct measure of psychology.
- This dashboard shows the top ten in each discipline. It does not include auction registration, price, fitness or role data.
""")
    st.info("The rankings are descriptive scouting evidence. They should be combined with role, availability, fitness and auction-price checks before a recruitment decision.")

st.markdown("---")
st.caption("PressurePlay · SupeRR Selector Season 2 · Round 1 | Analysis based on the supplied competition data pack.")
