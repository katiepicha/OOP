import RetailItemClass as ri

def main ():

    item1 = ri.RetailItem('Jacket',12,59.95)

    print('Item Description:', item1.get_description())
    print('Units in Inventory:', item1.get_units())
    print('Price:', item1.get_price())

    item2 = ri.RetailItem('Designer Jeans',40,34.95)

    print('Item Description:', item2.get_description())
    print('Units in Inventory:', item2.get_units())
    print('Price:', item2.get_price())

    item3 = ri.RetailItem('Shirt',20,24.95)

    print('Item Description:', item3.get_description())
    print('Units in Inventory:', item3.get_units())
    print('Price:', item3.get_price())

main()







