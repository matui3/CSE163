from cse163_utils import assert_equals
# Don't worry about this import syntax, we will talk about it later

import hw2_manual
import hw2_pandas
import csv



def test_parse():
    print(hw2_manual.parse('pokemon_test.csv', ['id']))

def test_species_count(data):
    x = 0

def test_max_level(data):
    print(hw2_manual.max_level(data))

def test_filter_range(data):
    print(hw2_manual.filter_range(data, 30, 70))

def test_mean_attack_type(data):
    print(hw2_manual.mean_attack_for_type(data, 'fire'))

def test_count_types(data):
    print(hw2_manual.count_types(data))


def main():
    data = hw2_manual.parse('pokemon_test.csv', ['id','level','atk','def','hp','stage'])
    # test_max_level(data)
    # test_filter_range(data)
    # test_parse()
    # test_species_count()
    # test_mean_attack_type(data)
    test_count_types(data)

# This file is left blank for you to fill in with your tests!
if __name__ =='__main__':
    main()
