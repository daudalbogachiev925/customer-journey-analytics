import os
import requests
import pandas as pd
import plotly.express as px
import streamlit as st

API = os.getenv("API_URL", "http://api:8000")
st.set_page_config(page_title="Journey Analytics", layout="wide")
st.title("Customer Journey Analytics")

@st.cache_data(ttl=15)
def fetch(path): return requests.get(f"{API}{path}").json()

st.subheader("Воронка")
default_steps = "app_open,signup_start,signup_complete,onboarding,first_value,purchase"
steps_input = st.text_input("Шаги (через запятую)", default_steps)
steps = [s.strip() for s in steps_input.split(",") if s.strip()]

if steps:
    funnel = requests.post(f"{API}/api/journeys/funnel", json=steps).json()
    df = pd.DataFrame(funnel)
    if not df.empty:
        st.plotly_chart(px.funnel(df, x="users", y="step"))
        st.dataframe(df)

st.subheader("Топ-путей")
paths = pd.DataFrame(fetch("/api/journeys/paths?top_n=10"))
if not paths.empty:
    st.dataframe(paths)

st.subheader("Что делают после события")
event = st.text_input("Событие", "app_open")
if event:
    next_events = pd.DataFrame(fetch(f"/api/journeys/next/{event}?top_n=10"))
    if not next_events.empty:
        st.plotly_chart(px.bar(next_events, x="event", y="count"))

st.subheader("Граф переходов")
edges = pd.DataFrame(fetch("/api/journeys/graph?top_edges=30"))
if not edges.empty:
    st.dataframe(edges)
