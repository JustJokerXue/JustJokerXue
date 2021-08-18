#5-8
peoples=['admin','bob','coco','alice','jack']
for people in peoples:
	if people=='admin':
		print("Hello admin,would you like to see a status report?")
	else:
		print("Hello "+people+",thank you for logging in again.")

#5-9
peoples=[]
if peoples:
	for people in peoples:
		if people=='admin':
			print("Hello admin,would you like to see a status report?")
		else:
			print("Hello "+people+",thank you for logging in again.")
else:
	print("We need to find some users!")


#5-10
current_users=['admin','bob','coco','alice','jack']
new_users=['Admin','tom','bob','tim','joker']
for new_user in new_users:
	if new_user.lower() in [current_user.lower() for current_user in current_users]:
		print("You need to think another name.")
	else:
		print("This name isn't been used.")

#5-11
numbers=[]
for value in range(1,10):
	numbers.append(value)
for number in numbers:
	if number==1:
		print(str(number)+"st")
	elif number==2:
		print(str(number)+"nd")
	elif number==3:
		print(str(number)+"rd")
	else:
		print(str(number)+"th")
