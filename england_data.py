import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file = "data//England_2021-02-23.csv"
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
    data["date"] = pd.to_datetime(df["date"])


def avg_age_of_death(data):
    day_groups = data.groupby(["date"])

    for name, group in day_groups:
        death_in_different_groups = group.loc[group['age_avg'] != -1, "deaths"]
        number_of_deaths_on_day = group.loc[group['age_avg'] != -1, "deaths"].sum()
        avg_age_in_groups = group.loc[group['age_avg'] != -1, "age_avg"]
        product = death_in_different_groups * avg_age_in_groups
        print("{} : {:0.2f}".format(name, product.sum() / number_of_deaths_on_day))


def sum_of_death_inAgeGroups(data, age_avg):
    day_groups = data.groupby(["date"])

    # for name, group in day_groups:
    #     death_in_different_groups = group.loc[group['age_avg'] != -1, "deaths"]
    #     death_in_different_groups = group.loc[(group['age_avg'] == age_avg) & (group['age_avg'] > 0), "deaths"]
    #     #print("{} {}:".format(name, death_in_different_groups.sum()))
    data = data.loc[(data['age_avg'] == age_avg)]
    return data


def sum_of_death_below_age(data, age):
    data = data.loc[(data['age_avg'] <= age & (data['age_avg'] > 0))]
    return data


def sum_of_death_above_age(data, age):


    data = data.loc[(data['age_avg'] > age & (data['age_avg'] > 0))]
    return data


clean_data(df)
# avg_age_of_death(df)
deaths_in_87 = sum_of_death_inAgeGroups(df, 87)
deaths = sum_of_death_inAgeGroups(df, 52)


def add_death_in_group(avg_age, deaths):
    deaths["deaths"].rolling(min_periods=7, window=7).sum()
    deaths["rollingSum"] = deaths["rollingSum"].fillna(0)
    maxDeath = max(deaths["rollingSum"])
    deaths["rollingSum"] = deaths["rollingSum"] / maxDeath
    sns.lineplot(data=deaths, x="date", y="rollingSum", label=avg_age)


def plot_some_groups():
    avg_age = 52
    add_death_in_group(avg_age, deaths=sum_of_death_inAgeGroups(df, avg_age))
    avg_age = 57
    add_death_in_group(avg_age, deaths=sum_of_death_inAgeGroups(df, avg_age))
    avg_age = 62
    add_death_in_group(avg_age, deaths=sum_of_death_inAgeGroups(df, avg_age))
    avg_age = 67
    add_death_in_group(avg_age, deaths=sum_of_death_inAgeGroups(df, avg_age))
    avg_age = 72
    add_death_in_group(avg_age, deaths=sum_of_death_inAgeGroups(df, avg_age))
    avg_age = 77
    add_death_in_group(avg_age, deaths=sum_of_death_inAgeGroups(df, avg_age))
    avg_age = 82
    add_death_in_group(avg_age, deaths=sum_of_death_inAgeGroups(df, avg_age))


def plot_more_age_groups():
    n = 70
    deaths_above = sum_of_death_above_age(df, n)
    print(deaths_above.head())
    add_death_in_group("Ü70", deaths=deaths_above)


plot_more_age_groups()

plt.show()
