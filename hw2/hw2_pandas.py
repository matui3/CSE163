
import pandas as pd

def species_count(df):
    name = df['name']
    species = set(name)
    return species

def max_level(df):
    level = df['level']
    max_level = max(level)
    name = df[df['level'] == max_level]['name'].values[0]
    return (name, max_level)

def filter_range(df, smallest, largest):
    pokemon_in_range = df[(df['level'] < largest) & (df['level'] >= smallest)]
    return list(pokemon_in_range['name'])

def mean_attack_for_type(type, df):
    attack_df = df[df['type'] == type]['atk']
    return (sum(attack_df)/len(attack_df))
    
def count_types(df):
    return df.groupby('type').size().to_dict()

def highest_stage_per_type(df):
    return df.groupby('type')['stage'].max().to_dict()

def mean_attack_per_type(df):
    return df.groupby('type')['atk'].mean().to_dict()

def main():
    df = pd.read_csv('pokemon_test.csv')
    # print(species_count(df))
    print(mean_attack_per_type(df))
    


# Write your functions here!
if __name__ == '__main__':
    main()
