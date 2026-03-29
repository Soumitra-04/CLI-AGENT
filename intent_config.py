intents =  {
    "play_music" : ["play", "listen", "song"],
    "open_app" : ["open", "launch", "start"],
    "send_message" : ["send", "message", "text"],
    "search_web" : ["search", "google", "find"],
    "exit" : ["exit", "bye", "quit"],
}

def intent_finder(user_input):
    input_list = user_input.lower().split()
    for word in input_list:
        for intent,keywords in intents.items():
            if(word in keywords):
                return intent
    
    return "ai"