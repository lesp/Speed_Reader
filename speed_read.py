from time import sleep

def clear():
    print("\n" *100)
    
with open ("text.txt", "r") as text:
    words = text.read()

list = words.split()

for i in list:
    clear()
    print(i)
    sleep(0.3)

    
