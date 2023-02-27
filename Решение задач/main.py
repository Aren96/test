import csv
import codecs

with codecs.open('Показания.csv', 'r', "utf_8_sig") as csvfile: # открываю csv файл
    reader = csv.DictReader(csvfile, delimiter=";") # читаю файл как dict сохраняю в переменную
    k = []  #  в пусты  list  беру чтобы в них собрать данные  для каждого месяца
    l = []
    q = []
    for row in reader:

        if  int(row['№ Квартиры']) != 0 : # ставлю условие чтобы взять только данные счетчика по квартирам
            k.append(row['Апрель']) # добавляю в лист
            l.append(row['Май'])
            q.append(row['Июнь'])
    k = sum([int(x) for x in k]) # суммирую данные каждой квартиры за определенный месяц
    l = sum([int(x) for x in l])
    q = sum([int(x) for x in q])

    print(f'потребление всей электроэнергии всех домов в Июнье {q}')
    print(f'потребление всей электроэнергии всех домов в Май {l}')
    print(f'потребление всей электроэнергии всех домов в Апрель {k}')
    print(f"общая сумма {k+l+q}")
w = k+l+q


with open("потребления.csv", "w",newline='') as csvfile:   #   создаю новый файл CSV
    writer = csv.writer(csvfile,delimiter=";")
    writer.writerow(["потребление всей электроэнергии всех домов в Июнье :"+str(q)])   #  добавляю простые строки так не смог writeheader пройтись и заголовки ставить
    writer.writerow(["потребление всей электроэнергии всех домов в  Майе:"+str(l)])
    writer.writerow(["потребление всей электроэнергии всех домов в Апрелье :"+str(k)])
    writer.writerow(["потребление всей электроэнергии за три месяца  :" + str(w)])




