import streamlit as st
import pandas as pd
import altair as alt

st.write('CMPD Traffic Stops')
st.write("Lara Kretschmer was here!")

stops = pd.read_csv("data/Officer_Traffic_Stops.csv")

st.dataframe(stops)