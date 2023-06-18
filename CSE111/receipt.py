import csv

def read_dictionary(filename, key):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary."""
    dictionary = {}
    name = 1
    price = 2

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            dictionary[row[key]] = row[key], row[name], row[price]
        print(dictionary)
    
    return dictionary
"""Parameters
    filename: the name of the CSV file to read.
    key_column_index: the index of the column
        to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

def main():
    key = 0
    name = 1
    price = 2
    products_dict = read_dictionary("products.csv", key)
    print(products_dict)
    with open("request.csv", "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        print("Requested Items")
        for row in reader:
            if row[key] in products_dict:
                print(f"{products_dict[row[key]][name]}: {row[1]} @ {products_dict[row[key]][price]}")

main()