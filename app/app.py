
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='Youth Unemployment Dashboard', layout='wide')

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('../data/world_bank/world_bank_dataset.csv', skiprows=4)
    df = df.drop(columns=['Indicator Name', 'Indicator Code'])
    df_long = df.melt(id_vars=['Country Name', 'Country Code'], var_name='Year', value_name='Youth Unemployment (%)')
    df_long['Year'] = pd.to_numeric(df_long['Year'], errors='coerce')
    df_long = df_long.dropna(subset=['Youth Unemployment (%)'])
    return df_long

df_long = load_data()

st.title("🌍 Youth Unemployment Dashboard (Ages 15–24)")
st.markdown("Compare youth unemployment rates across countries, over time, and visualize key trends.")

# Section: Dropdown for country selection
st.sidebar.header("Filter Countries")
all_countries = sorted(df_long['Country Name'].unique())
selected_countries = st.sidebar.multiselect("Select countries to compare:", all_countries, default=["South Africa", "Nigeria", "Germany"])

filtered = df_long[df_long['Country Name'].isin(selected_countries)]

# Section: Line chart comparison
st.subheader("📈 Youth Unemployment Trends by Country")
fig_line = px.line(filtered, x='Year', y='Youth Unemployment (%)', color='Country Name', markers=True)
st.plotly_chart(fig_line, use_container_width=True)

# Section: Choropleth animated map
st.subheader("🗺 Animated World Map of Youth Unemployment")
df_map = df_long[df_long['Year'] >= 2010]
fig_map = px.choropleth(df_map, locations="Country Code", color="Youth Unemployment (%)", 
                        hover_name="Country Name", animation_frame="Year",
                        color_continuous_scale="Reds", range_color=(0, 80),
                        title="Youth Unemployment Rate (15–24) by Country")
st.plotly_chart(fig_map, use_container_width=True)

# Section: Top 10 countries
st.subheader("🔝 Top 10 Countries by Youth Unemployment (Latest Year)")
latest_year = df_long['Year'].max()
latest = df_long[df_long['Year'] == latest_year].sort_values(by="Youth Unemployment (%)", ascending=False).head(10)
fig_bar = px.bar(latest, x='Youth Unemployment (%)', y='Country Name', orientation='h', title=f"Top 10 Countries ({int(latest_year)})")
st.plotly_chart(fig_bar, use_container_width=True)

# Section: Full sortable table
st.subheader("📊 Full Table - Youth Unemployment (Latest Year)")
latest_table = df_long[df_long['Year'] == latest_year].sort_values(by='Youth Unemployment (%)', ascending=False)
st.dataframe(latest_table.style.highlight_max(axis=0, color='salmon'))

# Optional: Download
st.sidebar.markdown("---")
st.sidebar.download_button("📥 Download CSV", data=df_long.to_csv(index=False), file_name='youth_unemployment_long.csv')
