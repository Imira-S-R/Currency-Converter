import functions

print('Welcome to Currency Converter Made By Imira Randeniya.')

def main () :
    print('''
1. Convert Currency    
2. View Available Currencies
3. QUIT    
    ''')

    option = int(input('> '))

    if option == 1:
        print('')
        currency_from = input('Enter symbol of the currency you have: ')
        currency_to = input('Enter symbol of currency you want to convert to: ')
        number = int(input('Enter amount to convert: '))
        result = functions.convert_currency(currency_from.upper(), currency_to.upper(), number)
        print('')
        print('RESULT')
        print(f'{str(result)} {currency_to.upper()}')
        print('')
        main()

    elif option == 2:
        functions.get_countries()
        main()

    elif option == 3:
        exit()

main()