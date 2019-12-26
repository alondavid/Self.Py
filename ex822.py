#ex 8.2.2

def key_func(s):
    return s[1]

def sort_prices(list_of_tuples):
    return sorted(list_of_tuples,key=key_func)

def main():
    products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
    print(sort_prices(products))

if __name__ == '__main__':
    main()
