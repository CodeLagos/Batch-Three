'''
Name ::: ADEPOJU BABATUNDE
Email ::: tunerio4u@gmail.com
Class ::: CodeLagos3 Python Class


        This program is designed to function as a calculator which adds the prices
        of items in your cart in succession and output the total value as total.
        should there be error in the computation ? the delete item can be used to
        to clear the cart and the calculation is started over again.'''





Cart=[]
Food={'Rice':250,'Beans':310,'Bread':200,'Yam':400}
Clothing={'Jean':1500,'Blouse':280,'T-shirt':1100,'Skirt':800}
Toiletries={'Tissue':200,'Soap':250,'Detergent':80,'Bleach':25,'Brush':150}
Drinks={'Soft-Drink':100,'Stout':300,'Beer':220,'Spirit':1800}


print("Welcome To Babz Store \nYour Sure Store For \nFoods \nClothing \nToiletries & \nDrinks")
print("Avaialable Items for Purchase include:::\nRice,Beans,Bread,Yam,Jean,Blouse,T-shirt,Skirt,Tissue,Soap,Detergent,Bleach,Brush,Soft-Drink,Stout,Beer,Spirit")


while(True):
    def add():
        #print("Welcome To CodeLagos Stores")
        ITEM = input("Item = ")
        QTY = int(input("Quantity = "))
        for i in Food.keys():
                if (ITEM.capitalize()== i):
                        Price=Food[i]*QTY
                        print('Price = ',Price)
                        Cart.append(Price)
        for i in Clothing.keys():
                if (ITEM.capitalize()== i):
                        Price=Clothing[i]*QTY
                        print('Price = ',Price)
                        Cart.append(Price)
        for i in Toiletries.keys():
                if (ITEM.capitalize()== i):
                        Price=Toiletries[i]*QTY
                        print('Price = ',Price)
                        Cart.append(Price)

        for i in Drinks.keys():
                if (ITEM.capitalize()== i):
                        Price=Drinks[i]*QTY
                        print('Price = ',Price)
                        Cart.append(Price)
    add()
    break
while (True):
    print ('Press 1 to add another Item \nPress 2 to Delete item  \nPress 3 to Get Total')
    
    Option=int(input('Enter Option\n'))       
    if (Option ==1):
             add()
            
    elif(Option==2):
        Cart.clear()
        print("Cart Cleared , Start Over Again")
        add()
    elif(Option==3):
            print('Total =',sum(Cart),'\nThanks For Your Patronage')
            break       

