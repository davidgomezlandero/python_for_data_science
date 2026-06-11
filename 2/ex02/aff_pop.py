import matplotlib.pyplot as plt
from load_csv import load


def parse_population(series):
    """
    Convert population values such as:
    '1.2k', '3.4M', '5.6B'
    into numeric values.
    """
    values = []

    for value in series:
        value = str(value)

        if value.endswith("k"):
            values.append(float(value[:-1]) * 1e3)
        elif value.endswith("M"):
            values.append(float(value[:-1]) * 1e6)
        elif value.endswith("B"):
            values.append(float(value[:-1]) * 1e9)
        else:
            try:
                values.append(float(value))
            except ValueError:
                values.append(None)

    return values


def main():
    """
    Display population comparison between Spain and United Kingdom.
    """
    data = load("population_total.csv")
    if data is None:
        return

    spain = data[data["country"] == "Spain"]
    uk = data[data["country"] == "United Kingdom"]

    if spain.empty or uk.empty:
        print("Country not found.")
        return

    years = [str(year) for year in range(1800, 2051)]

    spain_pop = parse_population(spain[years].iloc[0])
    uk_pop = parse_population(uk[years].iloc[0])

    plt.figure(figsize=(12, 6))

    plt.plot(years, spain_pop, label="Spain")
    plt.plot(years, uk_pop, label="United Kingdom", color="green")

    plt.title("Population Projection")
    plt.xlabel("Year")
    plt.ylabel("Population")

    plt.xticks(
        [str(year) for year in range(1800, 2051, 40)]
    )
    plt.yticks(
        [20e6, 40e6, 60e6, 80e6],
        ["20M", "40M", "60M", "80M"]
        )
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
