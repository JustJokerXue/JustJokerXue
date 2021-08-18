listdinner=['Bob','Joker','Tom']
print(listdinner[0]+","+listdinner[1]+" and "+listdinner[2]+",do you have time to eat dinner with me?")

print("Sorry,"+listdinner[1]+" can't attend for this dinner.")
listdinner[1]='Jack'
print(listdinner[0]+","+listdinner[1]+" and "+listdinner[2]+",do you have time to eat dinner with me?")
print("Everyone,I have found a bigger table!")
listdinner.insert(0,'Tim')
listdinner.insert(2,'Jerk')
listdinner.append('Bib')
print(listdinner[0]+","+listdinner[1]+","+listdinner[2]+","+listdinner[3]+","+listdinner[4]+" and "+listdinner[5]+",do you have time to eat dinner with me?")
print("Sorry,the new table I bought can't arrive,so I can only invite two friend.")
cant1=listdinner.pop(5)
print("Sorry,"+cant1+",I can't invite you to eat dinner with me.")
cant2=listdinner.pop(3)
print("Sorry,"+cant2+",I can't invite you to eat dinner with me.")
cant3=listdinner.pop(2)
print("Sorry,"+cant3+",I can't invite you to eat dinner with me.")
cant4=listdinner.pop(0)
print("Sorry,"+cant4+",I can't invite you to eat dinner with me.")
print(listdinner[0]+",you are still in the list that I invite friends.")
print(listdinner[1]+",you are still in the list that I invite friends.")
del listdinner[1]
print(listdinner)
del listdinner[0]
print(listdinner)

