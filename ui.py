import streamlit as st
import requests

st.set_page_config(layout = "wide")
url = "http://127.0.0.1:8000" # fastapi

resp = requests.get(url)
resp_json = resp.json()
msg = resp_json.get("message")
st.title(msg)
