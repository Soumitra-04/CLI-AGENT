from tools.notes import save_note
from brain import brain
from tools.whatsapp import whatsapp
from ai.llm import ask_ai
while(1):
    User_Input = input("Hello! How can I help you today? \n : ")
    output = brain(User_Input)
    if("exit" == output):
        break
    elif("note" == output):
           text = input("Enter the content: ")
           output_text = save_note(text)
           print(output)
    elif("whatsapp" == output):
        message = input("Enter your message: ")
        receiver = input("Enter the number of the receiver: ")
        whatsapp_output = whatsapp(receiver,message)
        print(whatsapp_output)
    elif(output == "ai"):
        ai_output = ask_ai(User_Input)
        print(ai_output)
    else:
        print("Sorry, I didn't understand! ")
    

