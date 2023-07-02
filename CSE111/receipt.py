import csv
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime
# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()
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
    price = 0
    count = 0
    sale_tax = 0.06
    try:
        products_dict = read_dictionary("products.csv", key)
        print('Inkom Emporium')
        print()
        with open("request.csv", "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                if row[key] in products_dict:
                    print(f"{products_dict[row[key]][name]}: {row[1]} @ {products_dict[row[key]][2]}")
                    pop_quantity = int({row[1]}.pop())
                    count = count + pop_quantity
                    pop_price = float({products_dict[row[key]][2]}.pop())
                    pop_price = pop_price * pop_quantity
                    price = price + pop_price
    except KeyError as keyerror:
        print(keyerror)
    except FileNotFoundError as file_error:
        print('Error: missing file')
        print(file_error)
        exit()
    sale_tax = sale_tax * price
    total = sale_tax + price
    print()
    print(f'Number of Items: {count}')
    print(f'Subtotal: {price:.2f}')
    print(f'Sales Tax: {sale_tax:.2f}')
    print(f'Total: {total:.2f}')
    print()
    print('Thank you for shopping at Inkom Emporium')
    print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")
main()