# pip install keyboard
import keyboard
import time

grpsize = int(input("This bot is designed to automate the actions needed to mention the members in a whatsapp group \nIt will tag all members irrespective of their position in the group \nYou will have have 5 seconds to place your cursor in the input box of your WhatsappWeb Window so it is recommended to keep that ready. \nEnter the size of your group including yourself \n"))
message = "@"
i = 0
print("you have 5 seconds to place your cursor")
time.sleep(5)  

while i < grpsize - 1:   
    keyboard.write(message) 
    for j in range(0, i + 1):
        keyboard.press_and_release('down')  
    keyboard.press_and_release('enter')  
    i += 1

keyboard.press_and_release('enter')