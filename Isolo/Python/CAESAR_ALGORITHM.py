'''CAESAR'S ALGORITHM FOR ENCRYPTING AND DECRYPTING MESSAGES BY ADEYINKA MICHAEL AYOOLUWA
        PHONE NO:08131244877
        EMAIL:ayomichaels16@gmail.com
        CLASS:CODE LAGOS PYTHON BATCH 3, CLASS1
        INSTRUCTOR:MR. CHIBOGWU EMMANUEL

    THIS LINES OF CODES HELPS USERS TO ENCRYPT AND DECRYPT MESSAGES,
    BY TAKING A MESSAGE AND THEN ENCRYPT OR DECRYPT WITH A KEY,
    WHICH THEN PRINTS OUT THE ENCRYPTED OR DECRYPTED MESSAGE'''

a='abcdefghijklmnopqrstuvwxyz '
def decrypt():
    while True:
        key=input('enter number to be used as key to decrypt: ')
        if key.isdigit():
            key=int(key)
            newMes=''
            mes=input('please enter a message: ')
            for character in mes:
                if character in mes:
                    pos=a.find(character)
                    new_pos=(pos-key)%27
                    new_char=a[new_pos]
                    #print('the new character is' ,new_char)
                    newMes+=new_char
            print('your decryted message is:', newMes)
            break
        else:
            print('error the key must be a number. Try again')

def encrypt():
    while True:
        key=input('enter number to be used as key to encrypt: ')
        if key.isdigit():
            key=int(key)
            newMes=''
            mes=input('please enter a message: ')
            for character in mes:
                if character in mes:
                    pos=a.find(character)
                    new_pos=(pos+key)%27
                    new_char=a[new_pos]
                    #print('the new character is' ,new_char)
                    newMes+=new_char
            print('your encrypted message is:', newMes)
            break
        else:
            print('error the key must be a number. Try again')

print(''' Welcome to Michaels Algorithm for Caesar. Select operation to be carried out.\n 1.\tEncrypt\n 2.\tDecrypt''')
while True:
    operation=input('enter desired operation 1 or 2: ')
    if (operation=='1'):
        encrypt()
    elif (operation=='2'):
        decrypt()
    else:
        print('error input either 1 or 2')
    

