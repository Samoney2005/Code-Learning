import pandas


data = pandas.read_csv("weather_data.csv")

#print(type(data))
print(type(data["temp"])) #series - 1 column
print((data["temp"]))

print("#_#_#__#_#_#__#_#__#_#_##__#_#_#_##__")

data_list = (data["temp"]).to_list()
print(data_list)
print(type(data_list))

#length of the list

print(len(data_list))


#convert data from pandas to a dictionnary
data_dict = (data["temp"]).to_dict()
print(data_dict)
print(type(data_dict))
