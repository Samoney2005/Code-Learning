import pandas


data = pandas.read_csv("weather_data.csv")

# The row for Tuesday
Tuesday = data[data["day"] == "Tuesday"]

#(data[data["day"] == "Tuesday"]).to_list()#

#print(type(Tuesday))
print(Tuesday)
#Listy = Tuesday.to_list()
Listy = Tuesday.day
#print(Listy)
#print(data[data["day"] == "Tuesday"])