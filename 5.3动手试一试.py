#5-3
alien_color='green'
if alien_color=='green':
	print("You have got 5 points.")
if alien_color=='red':
	print("You have got 5 points.")

#5-4	
alien_color='red'
if alien_color=='green':
	print("You have got 5 points.")
else :
	print("You have got 10 points.")

#5-5
alien_color='yellow'
if alien_color=='green':
	print("You have got 5 points.")
elif alien_color=='yellow':
	print("You have got 10 points.")
else:
	print("You have got 15 points.")

#5-6
age=19
if age<2 and age>=0:
	print("He is a baby.")
elif age<4:
	print("He is learning to walk.")
elif age<13:
	print("He is a child.")
elif age<20:
	print("He is a teen.")
elif age<65:
	print("He is a adult.")
else:
	print("He is a old people.")

#5-7
favourite_fruits=['tomato','apple','banana']
if 'potato' in favourite_fruits:
	print("You really like bananas!")
if 'abcd' in favourite_fruits:
	print("You really like bananas!")
if 'banana' in favourite_fruits:
	print("You really like bananas!")
