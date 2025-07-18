
# 🌍 Youth Unemployment Dashboard (Ages 15–24)

This project is a Streamlit-powered dashboard that visualizes global youth unemployment trends using data from the World Bank.

## 📌 Project Overview

The dashboard enables users to:
- Compare youth unemployment rates (ages 15–24) across multiple countries
- Explore animated maps of unemployment trends from 2010 to the present
- Identify top 10 countries with the highest unemployment
- View sortable tables with detailed statistics
- Download the full dataset as CSV

## 📊 Data Source

- **World Bank Indicator**: [SL.UEM.1524.ZS](https://data.worldbank.org/indicator/SL.UEM.1524.ZS)
- Youth Unemployment (% of labor force ages 15–24), yearly data per country

## 🧰 Tech Stack

- **Python**  
- **Streamlit**  
- **Pandas**  
- **Plotly Express**

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/LesibaFrans/youth-unemployment-data.git
cd youth-unemployment-data
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app/app.py
```

> 📁 Make sure to rename and place the World Bank dataset inside a `data/` folder:
> `data/world_bank/world_bank_dataset.csv`

## 📸 Dashboard Features

- 📈 Interactive line charts with country comparisons
- 🗺 Animated choropleth maps (2010–present)
- 🔝 Top 10 bar plot (latest year)
- 📊 Full country table with sorting/highlighting
- 📥 CSV download support

## 📫 Contact

- GitHub: [@lesiba-setsiba](https://github.com/LesibaFrans)
- Portfolio: [lesibafrans.github.io](https://lesibafrans.github.io/)
