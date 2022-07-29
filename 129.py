import csv

data = []
data2 = []
with open("C:/Users/aaron/Downloads\Project-127/scrapper.csv","r",encoding = "utf-8") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)
header1 = data[0]


with open("C:/Users/aaron/Downloads/Project-127/scrapper2.csv","r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        data2.append(i)
header2 = data2[0]

totalHeaders = header1+header2

planet_data = data[1: ]
planet_data2 = data2[1: ]

totalPlanet = []
for index, data in enumerate(planet_data):
    totalPlanet.append(planet_data[index]+planet_data2[index])


with open("C:/Users/aaron/Downloads/Project-127/totalPlanetData.csv","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(totalHeaders)
    csvwriter.writerows(totalPlanet)
