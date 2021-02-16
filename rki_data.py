import pandas as pd

file = "data//RKI_COVID19_15_02_2021.csv"
df = pd.read_csv(file)
print(df.info())

print(df["NeuerTodesfall"].unique())
print(df["NeuerTodesfall"].value_counts())


def death_per_day(data):
    death_per_day = data.groupby(["Meldedatum"])

    for name, group in death_per_day:
        deaths_in_group = group[(group["NeuerTodesfall"] >= 0) | (group["NeuerTodesfall"] == 1)]
        number_of_deaths = len(deaths_in_group.index)
        print("{} : {}".format(name, len(deaths_in_group)))


def fall_per_day(data):
    death_per_day = data.groupby(["Meldedatum"])

    for name, group in death_per_day:
        deaths_in_group = group[(group["NeuerFall"] >= 0) | (group["NeuerFall"] == 1)]
        print("{} : {}".format(name, len(deaths_in_group)))


fall_per_day(df)
