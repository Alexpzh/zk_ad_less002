# Представьте, что у вас есть таблица из 10 учеников с оценками учеников по 5 разным предметам.
# Вам нужно выполнить несколько шагов, чтобы проанализировать эти данные:
# 1. Самостоятельно создайте DataFrame с данными
# 2. Выведите первые несколько строк DataFrame, чтобы убедиться, что данные загружены правильно
# 3. Вычислите среднюю оценку по каждому предмету
# 4. Вычислите медианную оценку по каждому предмету
# 5. Вычислите Q1 и Q3 для оценок по математике:
# Q1_math = df['Математика'].quantile(0.25)
# Q3_math = df['Математика'].quantile(0.75)
# - можно также попробовать рассчитать IQR
# 6. Вычислите стандартное отклонение

import pandas as pd
#   1
df = pd.read_csv("pupils.csv")

#   2
print('\nВедомость по предметам:')
print (df.head())
print('\n\nОценки данных')
print(df.describe())

#   3
print('\nСредние оценки по предметам:\n')
for kk in df.keys():
    if kk == df.columns[0] or kk == df.columns[1]:
        continue
    print(f'{kk} средняя оценка: {df[kk].mean()}')

#   4
print('\nМедианные оценки по предметам:\n')
for kk in df.keys():
    if kk == df.columns[0] or kk == df.columns[1]:
        continue
    print(f'{kk} медианная оценка: {df[kk].median()}')

print('\n')
#   5
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
print(f'Квартиль 1 математика = {Q1_math}')
print(f'Квартиль 3 математика = {Q3_math}')
print(f'IQR математика = {Q3_math - Q1_math}')

#   6
print('\nСтандартные отклонения по предметам:\n')
for kk in df.keys():
    if kk == df.columns[0] or kk == df.columns[1]:
        continue
    print(f'{kk} стандартное отклонение: {df[kk].std():.2f}')


# №,Имя,Математика,Физика,Химия,Литература,История
# 1,Иванов И.И., 4, 3      , 5     , 4          , 3
# 2,Петров П.П., 5, 4      , 4     , 5          , 4
# 3,Сидоров С.С., 3, 3      , 4     , 3          , 5
# 4,Кузнецов К.К., 4, 5      , 3     , 4          , 4
# 5,Смирнов С.С., 5, 4      , 5     , 5          , 5
# 6,Попов П.П.  , 3, 4      , 4     , 3          , 4
# 7,Васильев В.В., 4, 3      , 3     , 4          , 3
# 8,Новиков Н.Н., 5, 5      , 4     , 5          , 5
# 9,Фёдоров Ф.Ф., 3, 3      , 5     , 3          , 4
# 10,Морозов М.М., 4, 4      , 3     , 5          , 3
