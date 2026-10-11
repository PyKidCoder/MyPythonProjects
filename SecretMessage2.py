import random

def even_odd_swap(x):
    if len(x) % 2 != 0:
        x = x + ' '

    even_letters = x[0::2]
    odd_letters = x[1::2]
    s = ' '

    for i in range(len(even_letters)):
        s = s+odd_letters[i]
        s = s+even_letters[i]

    return s


def swap_middle(x):
    if len(x) % 2 != 0:
        x = x + ' '

    first_half = x[0:int(len(x)/2):1]
    second_half = x[int(len(x)/2)::1]

    s = ''
    s = s + second_half
    s = s + first_half
    return s


def reverse(x):
    s = x[::-1]
    return s



letters = "abcdefghijklmnopqrstuvwxyz"


print ("ENEMY BASE IDENTIFIED")
print(" ________________")
print("|         <>     |")
print("|________________|")
print("SENDING COORDINATES")
print("PREPARE FOR BATTLE ⚔️")
print("WAIT!!")
print("THEY ARE SENDING SECRET MESSAGE")
print("TRYING TO DECODE")
print("")
print("")

def caesar_cipher(x, n):   
    s=''
    for i in range(len(x)):
        if x[i] == ' ':
            s = s + ' '
        else:
            idx = letters.find(x[i])
            new_idx = (idx+n)%26
            s = s + letters[new_idx]
    return s        

pbl = "attack"
secret_code = ""

for kk in range(10):
    n = random.randint(0, 25)
    secret_code = secret_code + letters[n]

pbl = pbl + secret_code

encoder = random.randint(0 , 1)

if encoder == 0:
    msg_enc = pbl
elif encoder == 1:
    msg_enc = even_odd_swap(pbl)


msg_enemy = caesar_cipher(msg_enc, random.randint(1, 25))
print(' I AM HEARING ...')
print(msg_enemy)
for kk in range(1, 26):
    msg_dec = caesar_cipher(msg_enemy, kk)
    msg_dec_eo = even_odd_swap(msg_dec)
    msg_dec_r  = reverse(msg_dec)
    msg_dec_sm = swap_middle(msg_dec)
   # print(msg_dec)

    if msg_dec[0:6:1]=='attack':
        print('CODE CRACKED ...')
      
        print('SECRET CODE IS ...')
        print(msg_dec[6::1])
        break
    elif msg_dec_eo[0:6:1]=='attack':
        print('CODE CRACKED ...')
       
        print('SECRET CODE IS ...')
        print(msg_dec_eo[6::1])
        break


    elif msg_dec_r[0:6:1]=='attack':
        print('CODE CRACKED ...')
       
        print('SECRET CODE IS ...')
        print(msg_dec_r[6::1])
        break

   
    elif msg_dec_sm[0:6:1]=='attack':
           print('CODE CRACKED ...')
           print('SECRET CODE IS ...')
           print (msg_dec_sm[6::1])
           
           break

print("PREPARE DEFENCES !! ")
print("THEY ARE ATTACKING")


print(secret_code)
print("ALERT ")
print(secret_code)
print("president !!")

    


    





