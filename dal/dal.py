import csv
import pandas as pd

class DAL:
    def __init__(self):
        pass


    def get_data(self):
        with open("../data/data.csv") as csvfile:
            print("Reading data from csv file the data")
            df = pd.read_csv("../data/data.csv", encoding="utf-8-sig")
        return df


    def get_weapons(self):
        weapons = []
        with open(r"..\data\weapon_list (1).txt") as csvfile:
            print("Reading data from csv file the weapons list")
            weapons = pd.read_csv(csvfile)
        return weapons


dd = DAL()
print(dd.get_data().head())
print(dd.get_data().head())