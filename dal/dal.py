import csv

class DAL:
    def __init__(self):
        pass


    def get_data(self):
        with open(r"C:\Users\gmth0\OneDrive\Desktop\data golan\Text_Malicious_ElasticSearch_12_WeekText_Malicious_ElasticSearch_12_Week\data\data.csv") as csvfile:
            print("Reading data from csv file the data")
            reader = csv.reader(csvfile)
        return reader


    def get_weapons(self):
        weapons = []
        with open(r"C:\Users\gmth0\OneDrive\Desktop\data golan\Text_Malicious_ElasticSearch_12_WeekText_Malicious_ElasticSearch_12_Week\data\weapon_list (1).txt") as csvfile:
            print("Reading data from csv file the weapons list")
            reader = csv.reader(csvfile)
        return weapons

#
# dd=DAL()
# print(dd.get_all_data())