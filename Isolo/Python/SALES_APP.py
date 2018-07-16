"""
SALES APP WITH PROFIT AND LOSS CALCULATOR BY OLAYIGBADE OLAWALE RAZAQ
            PHONE NUMBER:08093134270
            EMAIL:olayigbadeolawala@yahoo.com
            CLASS:CODE LAGOS PYTHON BATCH3,CLASS2
            INSTRUCTORS NAME: MR CHIBOGWU EMMANUEL & MR OYEDELE RIDWAN
    THIS LINE OF CODE HELP USER TO CALCULATE PROFIT AND LOSS ON SALES BY:
    1.CREATING AN ACCOUNT FOR THE USER
    2.LOGGING THE USER IN
    3.COLLECTING INPUT ON COST AND QUANTITY OF STOCKS
    4.COLLECTING INPUT ON COST AND QUANTITY OF SALES
    5.CALCULATING PROFIT AND LOSS ON EACH CATEGORIES OF PRODUCTS
    6.CALCULATING PROFIT AND LOSS ON TOTAL SALES
"""
import random
def CreateAccount():
    Sname = str(input("Enter User Surname Name\n"))
    Fname = str(input("Enter User FIrstname Name\n"))
    userID_no = random.randint(10000,99999)
    print("Account Created Sucessfully\n Firstname:", Fname, "\n Surname:", Sname, "\n User ID no:", userID_no)    
    CreatePassword = str(input("enter password:"))
    Re_enterPassword = str(input("re-enter password:"))
    if ( CreatePassword in Re_enterPassword ):
        print("Password created successfully")
    else:
        print("Password word does not match")
        CreateAccount()
    def logIn():
        ID_no = int(input("Please enter your ID no: "))
        if (ID_no == userID_no):
            print("correct")
        else:
            print("user does not esist")
            logIn()
        password = str(input("enter password: "))
        if (password == CreatePassword):
            print("correct")
        else:
            print("incorrect password")
            logIn()
        
    logIn()    
def StoreGoods():
    starting_cost = 0.0
    total_sales = 0.0
    dano_quantity = 0.0
    peak_quantity = 0.0
    cowbell_quantity = 0.0
    loya_quantity = 0.0
    bornvita_quantity = 0.0
    nescafe_quantity = 0.0
    milo_quantity = 0.0
    value_quantity = 0.0
    indomi_bellfull_quantity = 0.0
    hungry_man_quantity = 0.0
    menimi_quantity = 0.0
    chiki_chiki_quantity = 0.0
    coaster_quantity = 0.0
    cream_craker_quantity = 0.0
    pure_bliss_quantity = 0.0
    fiber_active_quantity = 0.0
    nasco_quantity = 0.0
    kalloges_quantity = 0.0
    infinity_quantity = 0.0
    funsnax_quantity = 0.0
    STotalCostOfMilk = 0.0
    TotalCostOfMilk = 0.0
    STotalCostOfTea = 0.0
    TotalCostOfTea = 0.0
    STotalCostOfNoodles = 0.0
    TotalCostOfNoodles = 0.0
    STotalCostOfBiscuit = 0.0
    TotalCostOfBiscuit = 0.0
    STotalCostOfCornFlakes = 0.0
    TotalCostOfCornFlakes = 0.0
    while True:
        print(" Perform store or sales \n \
                 \t Please choose the product you want to add to store\n \
              1. \t add Milk to store\n \
              2. \t add Tea to store\n \
              3. \t add Noodles to store\n \
              4. \t add Biscuit to store\n \
              5. \t add Corn flakes to store\n \
              6. \t sell Milk in store\n \
              7. \t sell Tea in store\n \
              8. \t sell Noodles in store\n \
              9. \t sell Biscuit in store\n \
              10. \t sell Corn flakes in store\n \
              11. \t Total cost and Total sales\n \
              12. \t PROFIT AND LOSS CALCULATOR\n \
              13. \t EXIT\n ")
        store = int(input("Responce please:"))    
        if (store == 1):
            print("Please add Milk to the store")
            dano_cost = int(input("Set cost price for Dano Milk: "))
            dano_quantity = int(input("Set quantity of Dano Milk: "))
            peak_cost = int(input("Set cost price for Peak Milk: "))
            peak_quantity = int(input("Set quantity of Peak Milk: "))
            cowbell_cost = int(input("Set cost price for Cowbell Milk: "))
            cowbell_quantity = int(input("Set quantity of Cowbell Milk: "))
            loya_cost = int(input("Set cost price for loya Milk: "))
            loya_quantity = int(input("Set quantity of Loya Milk: "))
            TotalCostOfMilk = ((dano_cost * dano_quantity) + (peak_cost * peak_quantity) + (cowbell_cost * cowbell_quantity) + (loya_cost * loya_quantity))
            starting_cost += TotalCostOfMilk
            print("The total cost of milk purchase is :", TotalCostOfMilk, "Naira")
            print("The total cost of goods is:", starting_cost)
        elif (store == 2):
            print("Please add Tea to the store")
            bornvita_cost = int(input("Set cost price for Bornvita: "))
            bornvita_quantity = int(input("Set quantity of Bornvita: "))
            nescafe_cost = int(input("Set cost price for Nescafe: "))
            nescafe_quantity = int(input("Set quantity of Nescafe: "))
            milo_cost = int(input("Set cost price for Milo: "))
            milo_quantity = int(input("Set quantity of Milo: "))
            value_cost = int(input("Set cost price for Value: "))
            value_quantity = int(input("Set quantity of Value: "))
            TotalCostOfTea = ((bornvita_cost * bornvita_quantity) + (nescafe_cost * nescafe_quantity) + (milo_cost * milo_quantity) + (value_cost * value_quantity))
            starting_cost += TotalCostOfTea
            print("The total cost of Tea purchase is :", TotalCostOfTea, "Naira")
            print("The total cost of goods is:", starting_cost)
        elif (store == 3):
            print("Please add Noodles to the store")
            indomi_bellfull_cost = int(input("Set cost  for INDOMI BELLEFUL: "))
            indomi_bellfull_quantity = int(input("Set quantity of INDOMI BELLEFUL: "))
            hungry_man_cost = int(input("Set cost price for HUNGRY MAN: "))
            hungry_man_quantity = int(input("Set quantity of HUNGRY MAN: "))
            menimi_cost = int(input("Set cost price for MENIMI: "))
            menimi_quantity = int(input("Set quantity of MENIMI: "))
            chiki_chiki_cost = int(input("Set cost price for CHIKI CHIKI: "))
            chiki_chiki_quantity = int(input("Set quantity of CHIKI CHIKI: "))
            TotalCostOfNoodles = ((indomi_bellfull_cost * indomi_bellfull_quantity) + (hungry_man_cost * hungry_man_quantity) + (menimi_cost * menimi_quantity) + (chiki_chiki_cost * chiki_chiki_quantity))
            starting_cost += TotalCostOfNoodles
            print("The total cost of Noodles purchase is :", TotalCostOfNoodles, "Naira")
            print("The total cost of goods is:", starting_cost)
        elif (store == 4):
            print("Please add Biscuit to the store")
            coaster_cost = int(input("Set cost price for Coaster: "))
            coaster_quantity = int(input("Set quantity of Coaster: "))
            cream_craker_cost = int(input("Set cost price for Cream Craker: "))
            cream_craker_quantity = int(input("Set quantity of Cream Craker: "))
            pure_bliss_cost = int(input("Set cost price for Pure Bliss: "))
            pure_bliss_quantity = int(input("Set quantity of Pure Bliss: "))
            fiber_active_cost = int(input("Set cost price for Fiber Active: "))
            fiber_active_quantity = int(input("Set quantity of Fiber Active: "))
            TotalCostOfBiscuit = ((coaster_cost * coaster_quantity) + (cream_craker_cost * cream_craker_quantity) + (pure_bliss_cost * pure_bliss_quantity) + (fiber_active_cost * fiber_active_quantity))
            starting_cost += TotalCostOfBiscuit
            print("The total cost of Biscuit purchase is :", TotalCostOfBiscuit, "Naira")
            print("The total cost of goods is:", starting_cost)
        elif (store == 5):
            print("Please add Cornflakes to the store")
            nasco_cost = int(input("Set cost price for Nasco: "))
            nasco_quantity = int(input("Set quantity of Nasco: "))
            kalloges_cost = int(input("Set cost price for Kalloges: "))
            kalloges_quantity = int(input("Set quantity of kalloges: "))
            infinity_cost = int(input("Set cost price for infinity: "))
            infinity_quantity = int(input("Set quantity of infinity: "))
            funsnax_cost = int(input("Set cost price for Funsnax: "))
            funsnax_quantity = int(input("Set quantity of Funsnax: "))
            TotalCostOfCornFlakes = ((nasco_cost * nasco_quantity) + (kalloges_cost * kalloges_quantity) + (infinity_cost * infinity_quantity) + (funsnax_cost * funsnax_quantity))
            starting_cost += TotalCostOfCornFlakes
            print("The total cost of cornflakes purchase is :", TotalCostOfCornFlakes, "Naira")
            print("The total cost of goods is:", starting_cost)
        elif (store == 6):
            print("Please enter cost and quantity of Milk sold")
            Sdano_cost = int(input("Set selling price for Dano Milk: "))
            Sdano_quantity = int(input("Set quantity of Dano Milk: "))
            Speak_cost = int(input("Set selling price price for Peak Milk: "))
            Speak_quantity = int(input("Set quantity of Peak Milk: "))          
            Scowbell_cost = int(input("Set selling price price for Cowbell Milk: "))
            Scowbell_quantity = int(input("Set quantity of Cowbell Milk: "))
            Sloya_cost = int(input("Set selling price price for loya Milk: "))
            Sloya_quantity = int(input("Set quantity of Loya Milk: "))
            if (Sdano_quantity > dano_quantity):
                print("Dano milk quantity demanded for is not available. Available stock is", dano_quantity )
            elif (Speak_quantity > peak_quantity):
                print("Peak milk quantity demanded for is not available. Available stock is", peak_quantity )
            elif (Scowbell_quantity > cowbell_quantity):
                print("cowbell milk quantity demanded for is not available. Available stock is", cowbell_quantity )
            elif (Sloya_quantity > loya_quantity):
                print("Loya milk quantity demanded for is not available. Available stock is", loya_quantity )
            else:
                STotalCostOfMilk = ((Sdano_cost * Sdano_quantity) + (Speak_cost * Speak_quantity) + (Scowbell_cost * Scowbell_quantity) + (Sloya_cost * Sloya_quantity))
                total_sales += STotalCostOfMilk
                print("The total Sales of milk purchase is :", STotalCostOfMilk, "Naira")
                print("The total sales of goods is:", total_sales)
        elif (store == 7):
            print("Please enter cost and quantity of Tea sold")
            Sbornvita_cost = int(input("Set selling price for Bornvita: "))
            Sbornvita_quantity = int(input("Set quantity of Bornvita: "))
            Snescafe_cost = int(input("Set selling price for Nescafe: "))
            Snescafe_quantity = int(input("Set quantity of Nescafe: "))
            Smilo_cost = int(input("Set selling price for Milo: "))
            Smilo_quantity = int(input("Set quantity of Milo: "))
            Svalue_cost = int(input("Set selling price for Value: "))
            Svalue_quantity = int(input("Set quantity of Value: "))
            if (Sbornvita_quantity > bornvita_quantity):
                print("Bornvita quantity demanded for is not available. Available stock is", bornvita_quantity )
            elif (Snescafe_quantity > nescafe_quantity):
                print("Nescafe quantity demanded for is not available. Available stock is", nescafe_quantity )
            elif (Smilo_quantity > milo_quantity):
                print("Milo quantity demanded for is not available. Available stock is", milo_quantity )
                                                    
            elif (Svalue_quantity > value_quantity):
                print("Value quantity demanded for is not available. Available stock is", value_quantity )
            else:
                STotalCostOfTea = ((Sbornvita_cost * Sbornvita_quantity) + (Snescafe_cost * Snescafe_quantity) + (Smilo_cost * Smilo_quantity) + (Svalue_cost * Svalue_quantity))
                total_sales += STotalCostOfTea
                print("The total Sales of Tea purchase is :", STotalCostOfTea, "Naira")
                print("The total sales of goods is:", total_sales)
        elif (store == 8):
            print("Please enter cost and quantity of Noodles sold")
            Sindomi_bellfull_cost = int(input("Set Selling INDOMI BELLEFUL for Bornvita: "))
            Sindomi_bellfull_quantity = int(input("Set quantity of INDOMI BELLEFUL: "))
            Shungry_man_cost = int(input("Set Selling price for HUNGRY MAN: "))
            Shungry_man_quantity = int(input("Set quantity of HUNGRY MAN: "))
            Smenimi_cost = int(input("Set Selling price for MENIMI: "))
            Smenimi_quantity = int(input("Set quantity of MENIMI: "))
            Schiki_chiki_cost = int(input("Set Selling price for CHIKI CHIKI: "))
            Schiki_chiki_quantity = int(input("Set quantity of CHIKI CHIKI: "))
            if (Sindomi_bellfull_quantity > indomi_bellfull_quantity):
                print("Indomi Bellfull quantity demanded for is not available. Available stock is", indomi_bellfull_quantity )
            elif (Shungry_man_quantity > hungry_man_quantity):
                print("Hungryman quantity demanded for is not available. Available stock is", hungry_man_quantity )
            elif (Smenimi_quantity > menimi_quantity):
                print("Menimi quantity demanded for is not available. Available stock is", menimi_quantity )
            elif (Schiki_chiki_quantity > chiki_chiki_quantity):
                print("Chiki Chiki quantity demanded for is not available. Available stock is", chiki_chiki_quantity )
            else:
                STotalCostOfNoodles = ((Sindomi_bellfull_cost * Sindomi_bellfull_quantity) + (Shungry_man_cost * Shungry_man_quantity) + (Smenimi_cost * Smenimi_quantity) + (Schiki_chiki_cost * Schiki_chiki_quantity))
                total_sales += STotalCostOfNoodles
                print("The total Sales of Noodles purchase is :", STotalCostOfNoodles, "Naira")
                print("The total sales of goods is:", total_sales)
        elif (store == 9):
            print("Please enter cost and quantity of Biscuit sold")
            Scoaster_cost = int(input("Set selling price for Coaster: "))
            Scoaster_quantity = int(input("Set quantity of Coaster: "))
            Scream_craker_cost = int(input("Set selling price for Cream Craker: "))
            Scream_craker_quantity = int(input("Set quantity of Cream Craker: "))
            Spure_bliss_cost = int(input("Set selling price for Pure Bliss: "))
            Spure_bliss_quantity = int(input("Set quantity of Pure Bliss: "))
            Sfiber_active_cost = int(input("Set selling price for Fiber Active: "))
            Sfiber_active_quantity = int(input("Set quantity of Fiber Active: "))
            if (Scoaster_quantity > coaster_quantity):
               print("Coaster quantity demanded for is not available. Available stock is", coaster_quantity ) 
            elif (Scream_craker_quantity > cream_craker_quantity):
                print("Cream Craker demanded for is not available. Available stock is", cream_craker_quantity )
            elif (Spure_bliss_quantity > pure_bliss_quantity):
                print("Purebliss quantity demanded for is not available. Available stock is", pure_bliss_quantity )
            elif (Sfiber_active_quantity > fiber_active_quantity):
                print("Fiberactive quantity demanded for is not available. Available stock is", fiber_active_quantity )        
            else:
                STotalCostOfBiscuit = ((Scoaster_cost * Scoaster_quantity) + (Scream_craker_cost * Scream_craker_quantity) + (Spure_bliss_cost * Spure_bliss_quantity) + (Sfiber_active_cost * Sfiber_active_quantity))
                total_sales += STotalCostOfBiscuit
                print("The total sales of Biscuit purchase is :", STotalCostOfBiscuit, "Naira")
                print("The total sales of goods is:", total_sales)
        elif (store == 10):
            print("Please enter cost and quantity of Cornflakes sold")
            Snasco_cost = int(input("Set cost price for Nasco: "))
            Snasco_quantity = int(input("Set quantity of Nasco: "))
            Skalloges_cost = int(input("Set cost price for Kalloges: "))
            Skalloges_quantity = int(input("Set quantity of kalloges: "))
            Sinfinity_cost = int(input("Set cost price for infinity: "))
            Sinfinity_quantity = int(input("Set quantity of infinity: "))
            Sfunsnax_cost = int(input("Set cost price for Funsnax: "))
            Sfunsnax_quantity = int(input("Set quantity of Funsnax: "))
            if (Snasco_quantity > nasco_quantity):
               print("Nasco quantity demanded for is not available. Available stock is", nasco_quantity ) 
            elif (Skalloges_quantity > kalloges_quantity):
                print("Kalloges quantity demanded for is not available. Available stock is", kalloges_quantity )
            elif (Sinfinity_quantity > infinity_quantity):
                print("Infinity quantity demanded for is not available. Available stock is", infinity_quantity )
            elif (Sfunsnax_quantity > funsnax_quantity):
                print("Funsnax quantity demanded for is not available. Available stock is", funsnax_quantity )
            else:
                STotalCostOfCornFlakes = ((Snasco_cost * Snasco_quantity) + (Skalloges_cost * Skalloges_quantity) + (Sinfinity_cost * Sinfinity_quantity) + (Sfunsnax_cost * Sfunsnax_quantity))
                total_sales += STotalCostOfCornFlakes
                print("The total sales of cornflakes purchase is :", STotalCostOfCornFlakes, "Naira")
                print("The total sales of goods is:", total_sales)
        elif (store == 11):
            print("goods successfully stored")
            print("The total cost of your stored goods is: ",starting_cost )
            print("The total sales of goods is:", total_sales)
        elif (store == 12):
            def profit_loss():
                print("PROFIT AND LOSS CALCULATOR")
                print("Please choose calculation \n \
                    1. \t Check profit or loss on MILK\n \
                    2. \t Check profit or loss on TEA\n \
                    3. \t Check profit or loss on NOODLES\n \
                    4. \t Check profit or loss on BISCUITS\n \
                    5. \t Check profit or loss on CORNFLAKES\n \
                    6. \t Check the TOTAL profit or loss\n ")
                check = int(input("Responce please: "))
                if (check == 1):
                    print("profit or loss on MILK")
                    MilkProfit_loss = STotalCostOfMilk - TotalCostOfMilk
                    if (MilkProfit_loss > 0):
                        print(" Your profit on MILK is: ", MilkProfit_loss)
                    else:
                        print("Your loss on MILK is: ", MilkProfit_loss)
                elif (check == 2):
                    print("profit or loss on TEA")
                    TeaProfit_loss = STotalCostOfTea - TotalCostOfTea
                    if (TeaProfit_loss > 0):
                        print(" Your profit on TEA is: ", TeaProfit_loss)
                    else:
                        print("Your loss on TEA is: ", TeaProfit_loss)
                elif (check == 3):
                    print("profit or loss on NOODLES")
                    NoodlesProfit_loss = STotalCostOfNoodles - TotalCostOfNoodles
                    if (NoodlesProfit_loss > 0):
                        print(" Your profit on NOODLES is: ", NoodlesProfit_loss)
                    else:
                        print("Your loss on NOODLES is: ", NoodlesProfit_loss)
                elif (check == 4):
                    print("profit or loss on BISCUITS")
                    BiscuitProfit_loss = STotalCostOfBiscuit - TotalCostOfBiscuit
                    if (BiscuitProfit_loss > 0):
                        print(" Your profit on BISCUITS is: ", BiscuitProfit_loss)
                    else:
                        print("Your loss on BISCUITS is: ", BiscuitProfit_loss)
                elif (check == 5):
                    print("profit or loss on CORNFLAKES")
                    CornFlakesProfit_loss = STotalCostOfCornFlakes - TotalCostOfCornFlakes
                    if (CornFlakesProfit_loss > 0):
                        print(" Your profit on CORNFLAKES is: ", CornFlakesProfit_loss)
                    else:
                        print("Your loss on CORNFLAKES is: ", CornFlakesProfit_loss)
                elif (check == 6):
                    print("TOTAL PROFIT OR LOSS ON SALES")
                    TotalProfit_loss = total_sales - starting_cost
                    if (TotalProfit_loss > 0):
                        print(" Your profit on your TOTAL SALES is: ", TotalProfit_loss)
                    else:
                        print(" Your loss on your TOTAL SALES is: ", TotalProfit_loss)
                else:
                        print("INVALID INPUT")
                        profit_loss()
            profit_loss()
        elif (store == 13):
                print("THANK YOU FOR USING OUR APPLICATION. WE LOVE TO SEE YOU AGAIN")
                break
        else:
            print("INVALID INPUT")
            StoreGoods()
            StoreGoods()
                          
print("WELCOME TO ABOKI SALES APP")
CreateAccount()
StoreGoods()
