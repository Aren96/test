import csv
import codecs

def hom_1(home_number,name_of_stret):
    with codecs.open('Показания.csv', 'r', "utf_8_sig") as csvfile:  # открываю csv файл
        reader = csv.DictReader(csvfile, delimiter=";")
        hom_values = []
        a = []
        for row in reader:

            if row['Улица'] == name_of_stret and int(row['№ дома']) == home_number and int(row['№ Квартиры']) != 0:
                hom_values.append(row['Апрель'])
                hom_values.append(row['Май'])
                hom_values.append(row['Июнь'])

            elif row['Улица'] == name_of_stret and int(row['№ дома']) == home_number and int(row['№ Квартиры']) == 0:
                a.append(row['Апрель'])
                a.append(row['Май'])
                a.append(row['Июнь'])
        hom_values=sum([int(x) for x in hom_values])
        a = sum([int(x) for x in a])
        if a!=hom_values:
            return (f'неверные значения в доме {home_number} на улице {name_of_stret} {hom_values} != {a}')
        else:
            return f'все хорошо {a} = {hom_values}'

print(hom_1(1,'Пушкина'))
print(hom_1(2,'Пушкина'))
print(hom_1(3,'Пушкина'))
print(hom_1(4,'Пушкина'))
print(hom_1(1,'Некрасова'))
print(hom_1(2,'Некрасова'))
print(hom_1(3,'Некрасова'))
print(hom_1(1,'Лермонтова'))
print(hom_1(2,'Лермонтова'))
print(hom_1(3,'Лермонтова'))






