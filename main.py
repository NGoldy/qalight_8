# створити список
mylist = [1, 3, 5, 4]
# сума всіх елементів списку
print("сума елементів")
s= mylist[0] + mylist[1] + mylist[2] + mylist[3]
print(s)
# список, в якому деякі елементи повторюються
replist = [2, 5, 5, 4, 2, 3]
unique_replist = list(set(replist))
print('унікальні значення')
print(unique_replist)
print('сума унікальних значень списку')
print(sum(unique_replist))
# створення словаря
employee = {'age': 35, 'job': 'engineer', 'salary': 2800}
print(employee['salary'])
employee['salary'] = 2800 / 1.5
print("заробітна платня в 1.5 менша")
print(employee['salary'])









