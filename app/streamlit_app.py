import streamlit as st
import requests
import pandas as pd

st.title("US Birth Forecast Dashboard")

horizon = st.slider(
    "Forecast Horizon",
    min_value=1,
    max_value=30,
    value=7
)

if st.button("Generate Forecast"):

    res = requests.get(
        f"http://127.0.0.1:8000/forecast?horizon={horizon}"
    )

    data = res.json()

    st.write("Forecast Output")

    st.json(data)

    df = pd.DataFrame({
        "Day": range(
            1,
            len(data["forecast"]) + 1
        ),
        "Forecast": data["forecast"]
    })

    st.line_chart(
        df.set_index("Day")
    )