import pandas

data = pandas.read_csv("Squirrel_Data.csv")

# prints the fur color
print(data["Primary Fur Color"])

# prints the row where the fur is Gray
fur = data[data["Primary Fur Color"] =="Gray"]
print(fur)

# The rows total of the Gray Fur
total_rows = len(fur)
print(f"Total rows for Grey (fur): {total_rows}")

# ab = [1,2,3,4,5,6,7,8,9]
# elt = len(ab)
# print(elt)
