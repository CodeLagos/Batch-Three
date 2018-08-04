#Name: Adedotun Onasanya
import string
string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'

id_user=str(input('what is your name ?'))
sex= str(input('enter M for male or F for female '))
if sex=='m' or 'F' or sex=='f' or 'M':
   pass
else:
   str(input('enter M or F'))
phone= int(input('enter number '))
age=float(input('must be 18 years and above'))
if age>=18:
   print(id_user,
   	sex,
   	age,
   	phone,
   	'WELCOME'+ id_user)
else:
   print('you are not eligible')
