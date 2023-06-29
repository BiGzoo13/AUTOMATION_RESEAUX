import pandas as pd


data = pd.read_excel("C:\\Users\\kevin.ponce\\Desktop\\PYTHON\\Equipement_reseau.xlsx")

for index, ligne in data.iterrows():
    if "192.168.1.15" in ligne["IP"]:
        data.at[index, "IP"] = "10.0.0.1"
        print("\n")
        print("IP modifier avec succès")



data.to_excel("C:\\Users\\kevin.ponce\\Desktop\\PYTHON\\Equipement_reseau.xlsx",index=False, sheet_name="Feuil1")


print("\n")
print(data)

