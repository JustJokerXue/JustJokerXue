#4-10
my_foods=['pizza','falafel','carrot','cake']
print("The first three items in the list are:")
print(my_foods[:3])
print("\nThree items from the middle of the list are:")
print(my_foods[1:4])
print("\nThe last three items in the list are:")
print(my_foods[-3:])#print(my_foods[1:4])

#4-11
friend_pizzas=my_foods[:]
my_foods.append('tomato')
friend_pizzas.append('potato')
print("\nMy favourite pizzas are:")
for my_food in my_foods:
	print(my_food)
print("\nMy friend's favourite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza)

#4-12
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("\nMy favourite foods are:")
for value in my_foods:
	print(value)
print("\nMy friend's favourite foods are:")
for value in friend_foods:
	print(value)
