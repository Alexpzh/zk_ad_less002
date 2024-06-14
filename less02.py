import pandas as pd
import numpy as np

def sample1():
    dates = pd.date_range(start='2022-07-26', periods=10, freq='D')
    print(dates)

    values = np.random.rand(10)

    df = pd.DataFrame({'Date': dates, 'Value': values})

    df.set_index('Date', inplace=True)
    print ('\nДата фрейм:')
    print (df)

    month = df.resample('ME').mean()
    print ('\nДата фрейм (месяц):')
    print (month)

def sample2():
    data = {
                'name': ['Alice','Bob', 'Charlie', 'David', 'Eve'],
                'gender': ['female', 'male', 'male', 'male', 'female'],
                'department': ['HR', 'Engineering', 'Marketing', 'Engineering', 'HR']
    }

    df = pd.DataFrame(data)

    df['gender'] = df['gender'].astype('category')
    df['department'] = df['department'].astype('category')

    print(df['department'].unique())
    print(df['gender'].cat.categories)
    print(df['department'].cat.categories)

    print(df['gender'].cat.codes)

    df['department'] = df['department'].cat.add_categories(['Finance'])
    df['department'] = df['department'].cat.remove_categories(['HR'])
    print(df['department'].cat.categories)
    print(df['department'].cat.codes)

sample2()