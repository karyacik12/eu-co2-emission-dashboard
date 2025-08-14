# EU CO₂ Emission Dashboard

This project analyzes and visualizes CO₂ emissions across European countries from 2000 to 2020, using open data from the [EDGAR database](https://edgar.jrc.ec.europa.eu/).

## Features
- **Data Cleaning**: Filters Europe-specific data from the global dataset
- **Analysis Script**: Generates static plots of emission trends
- **Interactive Dashboard**: Allows users to explore emission trends by country (Streamlit + Plotly)

## Tech Stack
- Python
- pandas, matplotlib, seaborn, plotly, streamlit

## How to Run
1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download `EU_emissions.csv` from [EDGAR](https://edgar.jrc.ec.europa.eu/) and place it in `data/` folder
4. Run analysis:
   ```bash
   python analysis.py
   ```
5. Launch dashboard:
   ```bash
   streamlit run dashboard.py
   ```

## Example Visualization
![Emission Trends](emission_trends.png)
