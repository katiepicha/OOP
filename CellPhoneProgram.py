import CellPhoneClass as cp

def main():
    manufact = input('Enter cell phone manufacturer: ')
    model = input('Enter cell phone model: ')
    retail_price = input('Enter retail price: ')

    phone = cp.CellPhone(manufact,model,retail_price)

    print('Here is your phone data:')
    print('Cell Phone Manufacturer:', phone.get_manufact())
    print('Cell Phone Model:', phone.get_model())
    print('Retail Price:', phone.get_retail_price())


main()
