import pandas as pd
import urllib.request, json
#url="https://opendata.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0.geojson"
#with urllib.request.urlopen(url) as url:
#    data = json.loads(url.read().decode())
#    print(data)
file="data//England_2021-02-14.csv"
df = pd.read_csv(file,nrows=1000)
print(df.info())

def death_per_day(data):
    death_per_day=data.groupby(["date"])

    for name,group in death_per_day:
        #print(group)
        #print(group["NeuerTodesfall"])
        deaths_in_group = group[(group["deaths"]>=0)]
        number_of_deaths = len(deaths_in_group.index)
        print("{} : {}".format(name,  len(deaths_in_group)))


death_per_day(df)
