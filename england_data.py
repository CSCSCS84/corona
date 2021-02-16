import pandas as pd

file = "data//England_2021-02-14.csv"
df = pd.read_csv(file)
print(df.info())


def clean_data(data):
    data["age_avg"] = data["age"]
    data["age_avg"] = data["age_avg"].replace("00_04", 2)
    data["age_avg"] = data["age_avg"].replace("05_09", 7)
    data["age_avg"] = data["age_avg"].replace("10_14", 12)
    data["age_avg"] = data["age_avg"].replace("15_19", 17)
    data["age_avg"] = data["age_avg"].replace("20_24", 22)
    data["age_avg"] = data["age_avg"].replace("25_29", 27)
    data["age_avg"] = data["age_avg"].replace("30_34", 32)
    data["age_avg"] = data["age_avg"].replace("35_39", 37)
    data["age_avg"] = data["age_avg"].replace("40_44", 42)
    data["age_avg"] = data["age_avg"].replace("45_49", 47)
    data["age_avg"] = data["age_avg"].replace("50_54", 52)
    data["age_avg"] = data["age_avg"].replace("55_59", 57)
    data["age_avg"] = data["age_avg"].replace("60_64", 62)
    data["age_avg"] = data["age_avg"].replace("65_69", 67)
    data["age_avg"] = data["age_avg"].replace("70_74", 72)
    data["age_avg"] = data["age_avg"].replace("75_79", 77)
    data["age_avg"] = data["age_avg"].replace("80_84", 82)
    data["age_avg"] = data["age_avg"].replace("85_89", 87)
    data["age_avg"] = data["age_avg"].replace("00_59", -1)
    data["age_avg"] = data["age_avg"].replace("60+", -1)
    data["age_avg"] = data["age_avg"].replace("90+", 95)


def avg_age_of_death(data):
    day_groups = data.groupby(["date"])

    for name, group in day_groups:

        death_in_different_groups = group.loc[group['age_avg'] != -1, "deaths"]
        number_of_deaths_on_day = group.loc[group['age_avg'] != -1, "deaths"].sum()
        avg_age_in_groups = group.loc[group['age_avg'] != -1, "age_avg"]
        product = death_in_different_groups * avg_age_in_groups
        print("{} : {:0.2f}".format(name, product.sum() / number_of_deaths_on_day))


clean_data(df)
avg_age_of_death(df)
