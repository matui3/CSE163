import cse163_utils  # noqa: F401
# This is a hacky workaround to an unfortunate bug on macs that causes an
# issue with seaborn, the graphing library we want you to use on this
# assignment.  You can just ignore the above line or delete it if you are
# not using a mac!
# Add your imports and code here!

import pandas as pd

def compare_bachelors_1980(data):
    df = data[(data['Min degree'] != 'high school') & (data['Min degree'] != 'associate\'s')]
    df = df[df['Year'] == 1980]
    df = df[df['Sex'] != 'A']
    df = df[['Sex', 'Total']]
    return df

def top_2_2000s(data):
    df = data[(data['Year'] >= 2000) & (data['Year'] <= 2010)]
    df = df.groupby(['Min degree'])['Total']
    print(type(df))
    
    

    








def main():
    df = pd.read_csv('hw3-nces-ed-attainment.csv')
    top_2_2000s(df)



if __name__ == '__main__':
    main()
