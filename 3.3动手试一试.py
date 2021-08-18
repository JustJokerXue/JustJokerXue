# -*-coding:utf-8-* 
'''3-8'''
travel=['chengdu','chongqing','shanghai','changsha','hubei']
print(travel)
print(sorted(travel))
print(travel)
print(sorted(travel,reverse=True))
print(travel)
travel.reverse()
print(travel)
travel.reverse()
print(travel)
travel.sort()
print(travel)
travel.sort(reverse=True)
print(travel)

'''3-9'''
listdinner=['Bob','Joker','Tom']
print(len(listdinner))

'''3-10'''
research=['mountain','river','country','city','language']
print(research[0].title())
print(research[0].upper())
print(research[0].lower())
print(sorted(research))
print(sorted(research,reverse=True))
research.reverse()
print(research)
research.reverse()
print(research)
#title、upper、lower用于字符串和列表中单个元素（也即为字符串），对于列表整体无法使用
