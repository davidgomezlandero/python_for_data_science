import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    Display the relationship between life expectancy \
and gross domestic product.
    """
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life = load("life_expectancy_years.csv")

    income_1900 = income["1900"]
    life_1900 = life["1900"]
    # print((income["country"] == life["country"]).all())
    income_values_1900 = income_1900.values
    life_values_1900 = life_1900.values
    plt.scatter(income_values_1900, life_values_1900, label="1900")
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.xscale("log")
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
