# ** this is the name of the FILE , not the name of the class

import CoinClass as c


# The main function.
def main():
       # Create an object from the Coin class.
       my_coin = c.Coin()   # this creates an instance called 'my_coin' of the class 'Coin()'

       # Display the side of the coin that is facing up.
       print('This side is up:', my_coin.get_sideup())    # notice you do not have to supply the argument/parameter
       # This will return 'Heads' because that is what we initialized the sideup as.

       # Toss the coin.
       print('I am going to toss the coin ten times:')
       for count in range(10):
           my_coin.toss()

           my_coin.sideup = 'Heads'

           # Display the side of the coin that is facing up.
           print('This side is up:', my_coin.get_sideup())

           
           
# Call the main function.

main()
