cars = input('Введите названия автомобилей: ')
names = input('Введите имена владельцев: ')
list_of_cars = cars.split(' ')
list_of_names = names.split(' ')
list_of_cars.sort()
list_of_names.sort()
if len(list_of_names) == len(list_of_cars):
    print(list(zip(list_of_names, list_of_cars)))
else:
    print('Списки не одинаковы.')