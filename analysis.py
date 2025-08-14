import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_prepare_data(file_path):
    df = pd.read_csv(file_path)
    df = df[(df['Region'] == 'Europe') & (df['Year'] >= 2000)]
    total_emissions = df.groupby(['Country', 'Year'])['Emissions'].sum().reset_index()
    return total_emissions

def plot_emission_trends(data):
    plt.figure(figsize=(12,6))
    sns.lineplot(data=data, x="Year", y="Emissions", hue="Country")
    plt.title("2000–2020 CO₂ Emission Trends in Europe")
    plt.ylabel("Million Tons of CO₂")
    plt.xlabel("Year")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig("emission_trends.png")
    plt.show()

if __name__ == "__main__":
    emissions_data = load_and_prepare_data("data/EU_emissions.csv")
    plot_emission_trends(emissions_data)
