import csv


def parse(file_name, int_cols):
    """
    Parses the CSV file specified by file_name and returns the data as a list
    of dictionaries where each row is represented by a dictionary that
    has keys for each column and value which is the entry for that column
    at that row.

    Also takes a list of column names that should have the data for that column
    converted to integers. All other data will be str.
    """
    data = []
    with open(file_name) as f:
        headers = f.readline().strip().split(',')
        num_cols = len(headers)

        for line in f.readlines():
            row_data = line.strip().split(',')
            row = {}
            for i in range(num_cols):
                if headers[i] in int_cols:
                    row[headers[i]] = int(row_data[i])
                else:
                    row[headers[i]] = row_data[i]
            data.append(row)
    return data


# Write your solutions here!
def species_count(data):
    name_set = set()
    for dict in data:
        name = dict.get('name')
        name_set.add(name)
    return len(name_set)

def max_level(data):
    name = ""
    max_level = 0
    for dict in data:
        level = dict.get('level')
        if (max_level < level):
            max_level = level
            name = dict.get('name')
    return (name, max_level)

def filter_range(data, smallest, largest):
    pokemon_list = []
    for dict in data:
        level = dict.get('level')
        if (level > smallest and level < largest):
            name = dict.get('name')
            pokemon_list.append(name)
    return pokemon_list

def mean_attack_for_type(data, type):
    total_atk = 0
    num_of_pokemon = 0
    for dict in data:
        pokemon_type = dict.get('type')
        if (type == pokemon_type):
            num_of_pokemon += 1
            atk = dict.get('atk')
            total_atk += atk
    if (total_atk != 0):
        return total_atk/num_of_pokemon
    else:
        return None
    
def count_types(data):
    types = {}
    for dict in data:
        count = 1
        pokemon_type = dict.get('type')
        if (pokemon_type in types):
            count += 1
            types[pokemon_type] = count
        else:
            types[pokemon_type] = count
    return types