import pandas as pd
import streamlit as st
import plotly.express as px

@st.cache_data
def load_data():
    df = pd.read_csv("data/EU_emissions.csv")
    df = df[(df['Region'] == 'Europe') & (df['Year'] >= 2000)]
    total_emissions = df.groupby(['Country', 'Year'])['Emissions'].sum().reset_index()
    return total_emissions

st.title("EU CO₂ Emission Dashboard")
st.markdown("Explore CO₂ emission trends across European countries (2000–2020).")

data = load_data()
country = st.selectbox("Select a country:", data['Country'].unique())

filtered = data[data['Country'] == country]
fig = px.line(filtered, x="Year", y="Emissions",
              title=f"{country} CO₂ Emissions (2000–2020)",
              labels={"Emissions": "Million Tons of CO₂", "Year": "Year"})

st.plotly_chart(fig)
