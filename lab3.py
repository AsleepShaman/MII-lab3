import csv;
import random;
import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt

#генерируем количество строк датасета
col = random.Random().randint(1000, 1500);

#данные
Names = ['Anna', 'Mary', 'Alex', 'John', 'Jozef', 'Oliver', 'Harry', 'Emma', 'Sophia', 'Isabella'];
Lastnames = ['Smith', 'Jones', 'Taylor', 'Williams','Brown','Davies','Evans','Wilson'];
Subdivs = ['sub-1', 'sub-2', 'sub-3', 'sub-4', 'sub-5', 'sub-6'];
JobTitle = ['Engineer', 'Physicist', 'Repairman', 'Geologist', 'Mathematician', 'Programmer'];

head = ['TabID', 'Name', 'Sex', 'Year of birth', 'Year of work', 'Subdivizion', 'Job title', 'Salary', 'Projects'];


#записываем датасет в csv файл
with open('lab3_data.csv', 'w', newline='') as f:
    writer = csv.writer(f);
    i = 1;
    writer.writerow(head);
    while i <= col:
        row = [10000+i, random.Random().choice(Names)+' '+random.Random().choice(Lastnames), random.Random().choice(['m', 'f']),
               random.Random().randrange(1970, 2004, 1), random.Random().randrange(1990, 2022, 1),  random.Random().choice(Subdivs),  random.Random().choice(JobTitle),
               random.Random().randrange(1000, 7000, 100), random.Random().randint(10, 100)];

        i = i + 1;
        writer.writerow(row);

prArr = [];
IDArr = [];
bthArr = [];
#массивы для графиков
jobArr = [];
sexArr = [];
jyArr = [];
#читаем датасет в лист
with open('lab3_data.csv') as f:
    reader = csv.reader(f);
    for row in reader:
        if(row[4] == 'Year of work'): continue;
        jyArr.append(row[4]);
        if(row[2] == 'Sex'): continue;
        sexArr.append(row[2]);
        if(row[6] == 'Job title'): continue;
        jobArr.append(row[6]);
        if(row[0] == 'TabID'): continue;
        IDArr.append(row[0]);
        if(row[3] == 'Year of birth'): continue;
        bthArr.append(row[3]);
        if(row[8] == 'Projects'): continue;
        prArr.append(row[8]);
        
prArr = sorted(list(map(int, prArr)));
bthArr = sorted(list(map(int, bthArr)));

def mediane(array):
    index = len(array) // 2;
    if len(array) % 2: 
        return array[index];
    return sum(map(int, array[index - 1:index + 1])) / 2;

print('\nСтатистические характеристики для количества проектов:');
print('Минимальное значение: ', min(prArr));
print('Максимальное значение: ', max(prArr));
print('Среднее значение: ', sum(prArr)//len(prArr));
print('Дисперсия: ', np.var(prArr));
print('Стандартное отклонение: ', np.std(prArr));
print('Медиана: ', mediane(prArr));
print('Мода: ', max((prArr.count(item), item) for item in prArr)[1]);

print('\nСтатистические характеристики для табельного номера:');
print('Минимальное значение: ', min(IDArr));
print('Максимальное значение: ', max(IDArr));
print('Медиана: ', mediane(IDArr));

print('\nСтатистические характеристики для года рождения:');
print('Минимальное значение: ', min(bthArr));
print('Максимальное значение: ', max(bthArr));
print('Среднее значение: ', sum(bthArr)//len(bthArr));
print('Дисперсия: ', np.var(bthArr));
print('Стандартное отклонение: ', np.std(bthArr));
print('Медиана: ', mediane(bthArr));
print('Мода: ',  max((bthArr.count(item), item) for item in bthArr)[1]);

#считываем данные в датафрейм
dataFrame = pd.read_csv('lab3_data.csv');

print('\nСТАТИСТИЧЕКИЕ ХАРАКТЕРИСТИКИ, ИСПОЛЬЗУЯ PANDAS');
print('\nСтатистические характеристики для количества проектов:');
print('Минимальное значение: ', dataFrame.min()['Projects']);
print('Максимальное значение: ', dataFrame.max()['Projects']);
print('Среднее значение: ', dataFrame.mean()['Projects']);
print('Дисперсия: ', dataFrame.var()['Projects']);
print('Стандартное отклонение: ', dataFrame.std()['Projects']);
print('Медиана: ', dataFrame.median()['Projects']);
print('Мода: ', dataFrame.mode()['Projects']);

print('\nСтатистические характеристики для табельного номера:');
print('Минимальное значение: ',dataFrame.min()['TabID']);
print('Максимальное значение: ', max(dataFrame['TabID']));
print('Медиана: ', dataFrame.median()['TabID']);

print('\nСтатистические характеристики для года рождения:');
print('Минимальное значение: ', dataFrame.min()['Year of birth']);
print('Максимальное значение: ',dataFrame.max()['Year of birth']);
print('Среднее значение: ', dataFrame.mean()['Year of birth']);
print('Дисперсия: ', dataFrame.var()['Year of birth']);
print('Стандартное отклонение: ', dataFrame.std()['Year of birth']);
print('Медиана: ', dataFrame.median()['Year of birth']);
print('Мода: ', dataFrame.mode()['Year of birth']);

#графики
m = 0;
f = 0;
for i in sexArr:
    if i == 'm': m = m + 1;
    else: f = f + 1;

plt.bar(['m', 'f'], [m, f])
plt.show()

e = 0; ph = 0; r = 0; g = 0; m = 0; pr = 0;
for j in jobArr:
    if j=='Engineer': e = e+1;
    if j=='Physicist': ph = ph+1;
    if j=='Repairman': r = r+1;
    if j=='Geologist': g = g+1;
    if j=='Mathematician': m = m+1;
    if j=='Programmer': pr = pr+1;
    
plt.pie([e, ph, r, g, m, pr], labels=JobTitle);
plt.show()

dataFrame['Year of work'].plot()
plt.show()






