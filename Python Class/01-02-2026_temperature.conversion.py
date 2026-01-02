import pandas

data = pandas.read_csv("weather_data.csv")

# The row for Wednesday
Wednesday = data[data["day"] == "Wednesday"]
print(Wednesday)

#Listy is assigned to temp
Listy = Wednesday.temp
print(Listy)

# Fahrenheit to Celsius Formula: C=(F-32)*5/9
Fahrenheit = Listy
Celsius = (Listy-32)*5/9
print(Celsius)
