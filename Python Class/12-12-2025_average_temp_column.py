import pandas


data = pandas.read_csv("weather_data.csv")

#convert data from pandas to a dictionnary
# Way 1: longer code without Pandas
data_list = (data["temp"]).to_list()

len_list = (len(data_list))
sum_list = sum(data_list)

result = sum_list/len_list
print(result)


#average of a series with pandas "mean()"
# Way 2: With Pandas finding the average
print(f'The mean is: {data["temp"].mean()}')

# This will give the max
print(f'The max is: {data["temp"].max()}')

# Way 3: Another way but just the sum not the average
'''
sum=0


for list in data_list:

    sum+=list # sum = sum + list

print(sum)
'''
