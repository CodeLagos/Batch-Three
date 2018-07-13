print("COOL MONEY FOREX LIMITED")
print ( 'NAME; AKINYEMI OLUMUYIWA BABAJIDE' )
print  ( 'CODE LAGOS IKORODU CENTER')
## This is a user guide to Cool money forex Currency Converter


print ( "select option '1'  For NGN to USD")
print ( "select option '2'  For NGN to GBP")
print ( "select option '3'  For NGN to ERU")
print ( "select option '4'  For NGN to AUD")
print ( "select option '5'  For NGN to CAD")

print ( "select option '6'  For USD to NGN")
print ( "select option '7'  For GBP to NGN")
print ( "select option '8'  For ERU to NGN")
print ( "select option '9'  For AUD to NGN")
print ( "select option '10'  For CAD to NGN")

# User should input the desired currency they wish to convert
user_input = input (" Select the option you want to process: ")
if user_input == '1':
    print("Convert NGN to USD")

    #User should input the values for NGN and USD
    NGN = int (input ("Input your currency value in NGN: "))
    # 359.50 NGN = 1 USD
    NGN_2_USD = NGN / 359.50
    print("Your currency's value in today Forex is (USD): " , round(NGN_2_USD,2))
    
    print("Thanks for choosing Cool money forex Currency Converter")

elif user_input == '2':
    print("Convert NGN to GBP")

    #User should input the values for NGN and GBP
    NGN = int (input ("Input your currency value in NGN: "))
    # 474.71 NGN = 1 GBP
    NGN_2_GBP = NGN / 474.71
    print("Your currency's value in today's Forex is (GBP): " , round(NGN_2_GBP,2))
    print ("===================================================================")
    print ("Thanks for choosing Cool money forex Currency Converter")

elif user_input == '3':
    print("Convert NGN to EUR")

    #User should input the values for NGN and EUR
    NGN = int (input ("Input your currency value in NGN: "))
    # 418.06 NGN = 1 EUR
    NGN_2_EUR = NGN / 418.06
    print("Your currency's value in today's Forex is (EUR): " , round(NGN_2_EUR,2))
    print("===================================================================")
    print("Thanks for choosing Cool money forex Currency Converter")

elif user_input == '4':
    print("Convert NGN to AUD")

    #User should input the values for NGN and AUD
    NGN = int (input ("Input your currency value in NGN: "))
    # 265.13 NGN = 1 AUD
    NGN_2_AUD = NGN / 265.13
    print("Your currency's value in today's Forex is (AUD): " , round(NGN_2_AUD,2))
    print("===================================================================")
    print("Thanks for choosing Cool money forex Currency Converter")

elif user_input == '5':
    print("Convert NGN to CAD")

    #User should input the values for NGN and CAD
    NGN = int (input ("Input your currency value in NGN: "))
    # 269.91 NGN = 1 CAD
    NGN_2_CAD = NGN / 269.91
    print("Your currency's value in today's Forex is (CAD): " , round(NGN_2_CAD,2))
    print("===================================================================")
    print("Thanks for choosing Cool money forex Currency Converter")

    
# User should input the desired currency they wish to convert

elif  user_input == '6':
    print("Convert USD to NGN")

    #User should input the values for USD to NGN
    USD = int (input ("Input your currency value in USD: "))
    # 359.50 NGN = 1 USD
    USD_2_NGN = USD* 359.50
    print("Your currency's value in today Forex is (NGN): " , (USD_2_NGN ))
    
    print("Thanks for choosing Cool money forex Currency Converter")

elif user_input == '7':
    print("Convert GBP to NGN")

    #User should input the values for GBP to NGN
    GBP = int (input ("Input your currency value in GBP: "))
    # 474.71 NGN = 1 GBP
    GBP_2_NGN = GBP*474.71
    print("Your currency's value in today's Forex is (NGN): " , GBP_2_NGN)
    print ("===================================================================")
    print ("Thanks for choosing Cool money forex Currency Converter")

elif user_input == '8':
    print("Convert EUR to NGN")

    #User should input the values for EUR to NGN 
    NGN = int (input ("Input your currency value in EUR: "))
    # 418.06 NGN = 1 EUR
    EUR_2_NGN = EUR*418.06
    print("Your currency's value in today's Forex is (NGN): " , EUR_2_NGN)
    print("===================================================================")
    print("Thanks for choosing Cool money forex Currency Converter")

elif user_input == '9':
    print("Convert AUD to NGN")

    #User should input the values for AUD to NGN
    AUD = int (input ("Input your currency value in AUD: "))
    # 265.13 NGN = 1 AUD
    AUD_2_NGN = AUDN*265.13
    print("Your currency's value in today's Forex is (NGN): " , AUD_2_NGN)
    print("===================================================================")
    print("Thanks for choosing Cool money forex Currency Converter")

elif user_input == '10':
    print("Convert NGN to CAD")

    #User should input the values for CAD to NGN 
    CAD = int (input ("Input your currency value in NGN: "))
    # 269.91 NGN = 1 CAD
    CAD_2_NGN = CAD*269.91
    print("Your currency's value in today's Forex is (NGN): " , CAD_2_NGN)
    print("===================================================================")
    print("Thanks for choosing Cool money forex Currency Converter")
    
    
