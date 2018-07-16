print ("Welcome to the temperature converter, please choose which measurement you want to convert TO")

which = input(" To convert TO a fahrenheit value, press f.        To convert TO a celcius value, press c.           To convert TO a kelvin value, press k.                                   If you want to convert TO a gas mark value, press g.")
if which == "f":
 print (" ")
 print ("Please choose the measurement you are converting FROM")
 fwhich = input("To convert FROM a celcius value, press c.        To convert FROM a kelvin value press k.           To convert FROM a gas mark value, press g.")
 if fwhich == "c":

  celcius = float(input("Please Input the celcius value: "))
  fahrenheit = (celcius*(9/5)+32)
  print ("In fahrenheit, this is " , fahrenheit)
 elif fwhich == "k":

  kelvin = float(input("Input the kelvin value: "))
  fahrenheit = (1.8 * (kelvin - 273) + 32)
  print ("In fahrenheit, this is " , fahrenheit)
 elif fwhich == "g":

  gasmark = float(input("Input the gas mark value: "))
  fahrenheit = 250 + (gasmark * 25)
  print ("In fahrenheit, this is " , fahrenheit)
 else:
  print (" ")
  print ("Error, you didn't enter any of the specified keys")
elif which == "c":
 print (" ")
 print ("please choose the measurement you are converting FROM")
 cwhich = input(" To convert FROM a fahrenheit value, press f.      To convert FROM a kelvin value, press k.          To convert FROM a gas mark value, press g.")
 if cwhich == "f":
  print (" ")
  fahrenheit = float(input("Please Input the fahrenheit value: "))
  celcius = (fahrenheit - 32)*(5/9)
  print ("In celcius, this is " , celcius)
 elif cwhich == "k":
  print (" ")
  kelvin = float(input("Please input the kelvin value: "))
  celcius = kelvin - 273
  print ("In celcius, this is " , celcius)
 elif cwhich == "g":
  print (" ")
  gasmark = float(input("Input the gas mark value: "))
  celcius = 130 + (gasmark * 10)
 else:
  print (" ")
  print ("Error, you didn't enter any of the specified keys")
elif which == "k":
 print (" ")
 print ("please choose the measurement you are converting FROM")
 kwhich = input("To convert FROM a fahrenheit value, press f.               To convert FROM a celcius value, press c.        To convert FROM a gas mark value, press g.")
 if kwhich == "f":
  print (" ")
  fahrenheit = float(input("Please input the fahrenheit value: "))
  kelvin = ((5/9) * (fahrenheit - 32) + 273)
  print ("In kelvin, this is " , kelvin)
 elif kwhich == "c":
  print (" ")
  celcius = float(input("Please input the celcius value: "))
  kelvin = (celcius + 273)
  print ("In kelvin, this is " , kelvin)
 elif kwhich == "g":
  print (" ")
  gasmark = float(input("Please input the gas mark value: "))
  kelvin = ((130 + (gasmark * 10))+ 273)
  print ("In kelvin, this is " , kelvin)
 else:
  print (" ")
  print ("Error, you didn't enter any of the specified keys")
elif which == "g":
 print (" ")
 print ("Please choose the measurement you are converting FROM")
 gwhich = input("To convert FROM a fahrenheit value, press f.                To convert FROM a celcius value, press c.           To convert FROM a kelvin value, press k.")
 if gwhich == "f":
  print (" ")
  fahrenheit = float(input("Please input the fahrenheit value: "))
  gasmark = (fahrenheit / 25) - 10
  print ("In gas mark, this is " , gasmark)
 elif gwhich == "c":
  print (" ")
  celcius = float(input("Input the celcius value: "))
  gasmark = ((celcius / 10) -13)
  print ("In gas mark, this is " , gasmark)
 elif gwhich == "k":
  print (" ")
  kelvin = float(input("Input the kelvin value: "))
  gasmark = (((kelvin - 273) / 10) -13) 
  print ("In gas mark, this is " , gasmark)
 else:
  print (" ")
  print ("Error, you didn't enter any of the specified keys")
else:
 print (" ")
 print ("Error, you didn't enter any of the specified keys")

