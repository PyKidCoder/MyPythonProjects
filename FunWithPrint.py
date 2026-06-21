import pyfiglet

print('\n')
print("Hello") 
playername = input ("What Is Your Name: ")
test = "Hello "+ playername;
#print(test + playername ) 
result = pyfiglet.figlet_format(test, font = ("bubble"))
print(result)
#print("hello  " + playername )  
mood = input ("How are you " + playername + "?" +'\n' )
#check the user input abd print response
if "good" in mood: print ("Iam good too")
elif "fine" in mood : print ("Iam fine too")
else: print ("its gonna be ok!\n")

answer = input("Should I tell you where iam learning these cool stuff?\n") 
if "yes" in answer: 
    print ("I learnt it on...")
    wibyte = pyfiglet.figlet_format("wibyte", font = ("bubble"))
    print (wibyte)

else: print("ok bye")