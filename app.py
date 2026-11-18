import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(page_title="PressurePlay | T20 scouting", page_icon="🏏", layout="wide")

ROOT = Path(__file__).parent
PAPER, INK, MUTED = "#f7f5ef", "#252b27", "#69716b"
GREEN, RUST, LINE = "#355b45", "#a34f38", "#deded5"

st.markdown(f"""
<style>
:root {{ color-scheme: light; }}
html, body, [data-testid="stAppViewContainer"], .stApp,
[data-testid="stHeader"], [data-testid="stMain"] {{
  background: {PAPER} !important; color: {INK} !important;
}}
[data-testid="stSidebar"] {{ background:#eeede6 !important; border-right:1px solid {LINE}; }}
[data-testid="stAppViewContainer"] *, [data-testid="stSidebar"] * {{ color:{INK} !important; }}
.stTextInput input, .stNumberInput input, .stTextArea textarea,
[data-baseweb="input"] input, [data-baseweb="textarea"] textarea,
[data-baseweb="select"] > div, [data-baseweb="popover"],
[data-baseweb="menu"], [role="listbox"], [role="option"] {{
  background:#ffffff !important; color:{INK} !important; border-color:#c9c9bf !important;
}}
/* All selectboxes across batting, bowling and comparison pages.
   Force a light surface on nested BaseWeb nodes as Streamlit may retain
   a dark widget background independently of the app canvas. */
[data-testid="stSelectbox"] [data-baseweb="select"],
[data-testid="stSelectbox"] [data-baseweb="select"] > div,
[data-testid="stSelectbox"] [data-baseweb="select"] div,
[data-testid="stSelectbox"] [data-baseweb="select"] span,
[data-testid="stSelectbox"] [data-baseweb="select"] input,
div[data-baseweb="popover"], div[data-baseweb="menu"],
div[data-baseweb="popover"] *, div[data-baseweb="menu"] *,
[role="listbox"], [role="option"], [role="listbox"] *, [role="option"] * {{
  background-color:#ffffff !important;
  color:{INK} !important;
  border-color:#c9c9bf !important;
  -webkit-text-fill-color:{INK} !important;
}}
[data-testid="stSelectbox"] svg {{ fill:{INK} !important; color:{INK} !important; }}
[data-testid="stWidgetLabel"] *, [data-testid="stMarkdownContainer"] *,
[data-testid="stCaptionContainer"] *, [data-testid="stMetric"] *,
[data-testid="stRadio"] *, [data-testid="stCheckbox"] *,
[data-testid="stSlider"] * {{ color:{INK} !important; }}
/* Consistent custom callout surfaces are used instead of theme-dependent alerts. */
.pp-callout {{
  background:#eaf0f2 !important;
  color:{INK} !important;
  border:1px solid #b8c8ce;
  border-left:4px solid {GREEN};
  border-radius:4px;
  padding:12px 15px;
  line-height:1.5;
}}
.pp-callout * {{ color:{INK} !important; -webkit-text-fill-color:{INK} !important; }}
.pp-warning {{
  background:#f5eee6 !important;
  color:{INK} !important;
  border:1px solid #d9c6b4;
  border-left:4px solid {RUST};
  border-radius:4px;
  padding:12px 15px;
}}
.pp-warning * {{ color:{INK} !important; -webkit-text-fill-color:{INK} !important; }}
input::placeholder, textarea::placeholder {{ color:#69716b !important; opacity:1 !important; }}
h1,h2,h3 {{font-family:Georgia,'Times New Roman',serif!important;color:{INK}!important;}}
.eyebrow {{color:{GREEN}!important;font-size:11px;letter-spacing:1.8px;text-transform:uppercase;}}
.deck {{color:{MUTED}!important;font-family:Georgia,serif;font-size:17px;line-height:1.45;}}
.rule {{border-top:1px solid {LINE};margin:14px 0 20px;}}
.note {{background:#efeee8;border-left:3px solid {RUST};padding:11px 14px;color:{INK}!important;}}
.note * {{color:{INK}!important;}}
div[data-testid="stMetric"] {{background:transparent;border-top:2px solid {GREEN};padding-top:9px;}}
[data-testid="stDataFrame"] {{border:1px solid {LINE};}}
.stButton button {{border-radius:3px;border:1px solid {GREEN};color:{GREEN}!important;background:#ffffff;}}
.stButton button * {{color:{GREEN}!important;}}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    return pd.read_csv(ROOT / "rankings.csv")

df = load_data()
bat = df[df.category.eq("Batter")].sort_values("rank").copy()
bowl = df[df.category.eq("Bowler")].sort_values("rank").copy()

def chart_style(fig, height=360):
    fig.update_layout(
        height=height, margin=dict(l=18,r=42,t=42,b=34),
        paper_bgcolor=PAPER, plot_bgcolor=PAPER,
        font=dict(color=INK), legend_title_text="",
        xaxis=dict(showgrid=True,gridcolor=LINE,zeroline=False),
        yaxis=dict(showgrid=False,zeroline=False)
    )
    return fig

def fmt_table(data, columns, names):
    return data[columns].rename(columns=names)

st.markdown('<div class="eyebrow">SupeRR Selector Season 2 · Round 1</div>', unsafe_allow_html=True)
st.title("PressurePlay")
st.markdown('<div class="deck">A scouting notebook on who holds their shape when a T20 innings gets difficult.</div>', unsafe_allow_html=True)
st.markdown('<div class="rule"></div>', unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### Match room")
    page = st.radio("Explore", ["Overview", "Batting rankings", "Bowling rankings", "Player comparison", "Methodology"])
    st.markdown("---")
    st.caption("Data window: 2022 to 1 November 2026")
    st.caption("Competitions: IPL and T20 Internationals")
    st.caption("Source: supplied SupeRR Selector data pack")
    st.caption("Displayed rankings: top 10 per discipline")

if page == "Overview":
    st.markdown("## At a glance")
    c1,c2,c3,c4 = st.columns(4)
    for col, value, label in [
        (c1,"837","matches in scope"),(c2,"193,988","deliveries analysed"),
        (c3,"69,326","batter-pressure balls"),(c4,"55,421","bowler-pressure balls")]:
        col.metric(label, value)
    left,right=st.columns([1.1,1])
    with left:
        st.markdown("### The short read")
        st.markdown("**Batting**")
        st.write("Fakhar Zaman leads the combined pressure ranking. Tim David has the largest pressure-ball sample among the top three, while Vaibhav Sooryavanshi records the highest pressure strike rate in the top ten.")
        st.markdown("**Bowling**")
        st.write("Sunil Narine leads the bowling list. Ravi Bishnoi has the largest pressure sample among the top five, giving his results a broader evidence base.")
    with right:
        st.markdown('<div class="note"><b>How to read these rankings</b><br>These are statistical pressure rankings, not auction availability recommendations. Role, registration, fitness and price require separate checks.</div>',unsafe_allow_html=True)
        st.markdown("### Leaders")
        st.write(f"**Batting:** {bat.iloc[0].player}")
        st.write(f"**Bowling:** {bowl.iloc[0].player}")
    a,b=st.columns(2)
    with a:
        st.markdown("### Pressure strike rate")
        f=px.bar(bat.sort_values("pressure_strike_rate"),x="pressure_strike_rate",y="player",orientation="h",
                 labels={"pressure_strike_rate":"Strike rate","player":""},text="pressure_strike_rate")
        f.update_traces(marker_color=GREEN,texttemplate="%{text:.1f}",textposition="outside",cliponaxis=False)
        st.plotly_chart(chart_style(f,390),use_container_width=True,config={"displayModeBar":False,"scrollZoom":False})
    with b:
        st.markdown("### Pressure economy")
        f=px.bar(bowl.sort_values("pressure_economy",ascending=False),x="pressure_economy",y="player",orientation="h",
                 labels={"pressure_economy":"Economy","player":""},text="pressure_economy")
        f.update_traces(marker_color=RUST,texttemplate="%{text:.2f}",textposition="outside",cliponaxis=False)
        st.plotly_chart(chart_style(f,390),use_container_width=True,config={"displayModeBar":False,"scrollZoom":False})

elif page == "Batting rankings":
    st.markdown("## Batters under pressure")
    st.caption("Rank order is based on average position under the core and relaxed pressure definitions. Displayed metrics use the core definition.")
    query=st.text_input("Find a batter",placeholder="Type a player name")
    minimum=st.slider("Minimum pressure balls",100,750,100,25)
    view=bat[(bat.pressure_balls>=minimum) & bat.player.str.contains(query,case=False,na=False)]
    st.dataframe(fmt_table(view,["rank","player","pressure_balls","pressure_innings","pressure_runs","pressure_strike_rate","pressure_average","pressure_innings_success_rate"],
        {"rank":"Rank","player":"Player","pressure_balls":"Balls","pressure_innings":"Innings","pressure_runs":"Runs","pressure_strike_rate":"Pressure SR","pressure_average":"Pressure average","pressure_innings_success_rate":"Consistency (%)"}),
        hide_index=True,use_container_width=True)
    if not view.empty:
        chosen=st.selectbox("Inspect player",view.player.tolist())
        r=bat[bat.player.eq(chosen)].iloc[0]
        m=st.columns(4)
        for col,label,val in zip(m,["Pressure SR","Pressure average","Pressure balls","Consistency"],[f"{r.pressure_strike_rate:.1f}",f"{r.pressure_average:.1f}",f"{int(r.pressure_balls):,}",f"{r.pressure_innings_success_rate:.1f}%"]):
            col.metric(label,val)
        st.markdown(
            f'<div class="pp-callout"><b>Player snapshot</b><br>{chosen} scored '
            f'{int(r.pressure_runs)} runs from {int(r.pressure_balls)} pressure balls '
            f'across {int(r.pressure_innings)} pressure innings in this sample.</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown('<div class="pp-warning">No player matches those filters.</div>', unsafe_allow_html=True)

elif page == "Bowling rankings":
    st.markdown("## Bowlers under pressure")
    st.caption("Lower pressure economy and bowling strike rate indicate better run control and wicket frequency.")
    query=st.text_input("Find a bowler",placeholder="Type a player name")
    minimum=st.slider("Minimum pressure balls",100,900,100,25)
    view=bowl[(bowl.pressure_balls>=minimum) & bowl.player.str.contains(query,case=False,na=False)]
    st.dataframe(fmt_table(view,["rank","player","pressure_balls","pressure_innings","pressure_wickets","pressure_economy","pressure_bowling_strike_rate","pressure_innings_success_rate"],
        {"rank":"Rank","player":"Player","pressure_balls":"Balls","pressure_innings":"Innings","pressure_wickets":"Wickets","pressure_economy":"Pressure economy","pressure_bowling_strike_rate":"Bowling SR","pressure_innings_success_rate":"Consistency (%)"}),
        hide_index=True,use_container_width=True)
    if not view.empty:
        chosen=st.selectbox("Inspect player",view.player.tolist())
        r=bowl[bowl.player.eq(chosen)].iloc[0]
        m=st.columns(4)
        for col,label,val in zip(m,["Pressure economy","Bowling SR","Pressure wickets","Consistency"],[f"{r.pressure_economy:.2f}",f"{r.pressure_bowling_strike_rate:.2f}",f"{int(r.pressure_wickets)}",f"{r.pressure_innings_success_rate:.1f}%"]):
            col.metric(label,val)
        st.markdown(
            f'<div class="pp-callout"><b>Player snapshot</b><br>{chosen} took '
            f'{int(r.pressure_wickets)} wickets from {int(r.pressure_balls)} pressure balls '
            f'across {int(r.pressure_innings)} pressure innings.</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown('<div class="pp-warning">No player matches those filters.</div>', unsafe_allow_html=True)

elif page == "Player comparison":
    st.markdown("## Compare players")
    discipline=st.radio("Discipline",["Batters","Bowlers"],horizontal=True)
    source=bat if discipline=="Batters" else bowl
    p1,p2=st.columns(2)
    with p1: one=st.selectbox("Player one",source.player.tolist(),index=0)
    with p2: two=st.selectbox("Player two",source.player.tolist(),index=min(1,len(source)-1))
    comp=source[source.player.isin([one,two])].copy()
    if discipline=="Batters":
        metrics=["pressure_strike_rate","pressure_average","pressure_innings_success_rate","pressure_balls"]
        labels=["Pressure strike rate","Pressure average","Consistency (%)","Pressure balls"]
    else:
        metrics=["pressure_economy","pressure_bowling_strike_rate","pressure_innings_success_rate","pressure_balls"]
        labels=["Pressure economy","Bowling strike rate","Consistency (%)","Pressure balls"]
    for metric,label in zip(metrics,labels):
        st.markdown(f"**{label}**")
        fig=px.bar(comp,x="player",y=metric,color="player",labels={"player":"","color":"Player",metric:label},text=metric)
        # Keep value labels within the available plotting area.
        fig.update_traces(textposition="outside", cliponaxis=False)
        max_value = float(comp[metric].max()) if not comp.empty else 0
        fig.update_yaxes(range=[0, max_value * 1.22 if max_value > 0 else 1])
        fig.update_layout(margin=dict(l=18, r=28, t=48, b=42))
        st.plotly_chart(chart_style(fig, 280), use_container_width=True,
                        config={"displayModeBar":False, "scrollZoom":False, "displaylogo":False})
    st.dataframe(comp[["rank","player"]+metrics].rename(columns={"rank":"Rank","player":"Player"}),hide_index=True,use_container_width=True)

else:
    st.markdown("## How the rankings were built")
    st.markdown("""
**Pressure is a match state, not simply the final overs.** The analysis labels pressure before each delivery, using chase rate, current rate, wickets in hand, balls remaining and innings stage. Batting and bowling have separate rules.

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

**Scope and limitations**
- IPL and T20 Internationals, 2022 to 1 November 2026.
- Eligibility threshold: at least 100 pressure balls and eight pressure innings.
- Pressure is a proxy based on match state, not a direct measure of psychology.
- This dashboard displays the top ten in each discipline.
- Auction registration, price, availability, fitness and role are not modelled.
""")
    st.markdown(
        '<div class="pp-callout"><b>Important interpretation note</b><br>'
        'Treat the rankings as descriptive scouting evidence. Combine them with role, '
        'availability, fitness and auction-price checks before making recruitment decisions.</div>',
        unsafe_allow_html=True
    )

st.markdown("---")
st.caption("PressurePlay · SupeRR Selector Season 2 · Round 1 | Derived metrics from the supplied competition data pack.")
