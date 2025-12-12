import pandas


data = pandas.read_csv("weather_data.csv")






#convert data from pandas to a dictionnary
data_list = (data["temp"]).to_list()

len_list = (len(data_list))
sum_list = sum(data_list)

result = sum_list/len_list
print(result)


#average of a series with pandas "mean()"

print(data["temp"].mean())




'''
sum=0


for list in data_list:

    sum+=list # sum = sum + list

print(sum)
'''
