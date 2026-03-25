
def brain(User_Input):
    if("whatsapp" in User_Input.lower()):
        return "whatsapp"
    elif("note" in User_Input.lower()):
        return "note"
    elif("exit" in User_Input.lower()):
        return "exit"
    
    return "ai"
    