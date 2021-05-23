import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("./pokemon.csv")
print(data)
print("#" * 80)

namedView = data.set_index("Name")
print(namedView[["HP", "Attack", "Defense"]])
#print(namedView[["HP", "Attack", "Defense"]][namedView["HP"] > 100])
print("#" * 80)

data["Offensive"] = data["Attack"] + data["Sp. Atk"]
data["Defensive"] = data["Defense"] + data["Sp. Def"]

print(data.head(2))
print(namedView.head(2))
print("#" * 80)

# SELECT DISTINCT * FORM
#    SELECT Type_1 FROM data WHERE Generation == 1
#    UNION
#    SELECT Type_2 FROM data WHERE Generation == 1

print("All Types of Gen 1 Pokémon")

gen1View  = data[ data["Generation"] == 1]
gen1Types = pd.concat( [gen1View["Type 1"], gen1View["Type 2"]] ).dropna()

print(gen1Types.unique())
print("#" * 80)

groupedByType1 = namedView.groupby("Type 1")
groupMeans = groupedByType1.mean().sort_values("Total", ascending=False)
print(groupMeans.head(10))
print("#" * 80)

relMeanDeviation = lambda x : (x - np.mean(x)) / np.mean(x)
cols = data.columns[4:]   # all non-string columns

relativeData = data[cols].transform(relMeanDeviation)

print(relativeData.head(5))
print("#" * 80)

boundaries = np.linspace( data.Total.min(), data.Total.max(), 11 )
bins = pd.cut(namedView["Total"], boundaries)

print("Charizard is in bin: ", bins["Charizard"])
print("Pokémon in the same bin:")
print(namedView[bins == bins["Charizard"]].index)
print("#" * 80)

for x in data :
    print(x)
print("#" * 80)

for i, x in enumerate(data.iteritems()) :
    if i < 1 : continue
    print(x)
    if i > 1 : break
print("#" * 80)

for x in data.iterrows() :
    print(x)
    break
print("#" * 80)

for x in data.itertuples() :
    print(x)
    break

data.plot()
plt.xlabel("Pokémon ID")
plt.ylabel("Status")
plt.show()

data["Attack"].plot()
plt.xlabel("Pokémon ID")
plt.ylabel("Attack")
plt.show()