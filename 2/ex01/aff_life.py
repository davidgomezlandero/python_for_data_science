import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    Display life expectancy in Spain.
    """
    data = load("life_expectancy_years.csv")
    if data is None:
        return

    spain = data[data["country"] == "Spain"]

    if spain.empty:
        print("Country not found.")
        return

    years = [int(year) for year in data.columns[1:]]
    life_expectancy = spain.iloc[0, 1:].astype(float)

    plt.figure(figsize=(12, 6))
    plt.plot(years, life_expectancy, label="Spain")

    plt.title("Spain Life expectancy Projections", fontsize=16)
    plt.xlabel("Year", fontsize=16)
    plt.ylabel("Life Expectancy", fontsize=16)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
