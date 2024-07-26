# Question 1: filter fruit with more than 5 alphabet

fruits = ['apple', 'banana', 'mango', 'Grapes', 'elderberry']
filtr_fruits = list(filter(lambda x: len(x) > 5, fruits))
print(filtr_fruits)