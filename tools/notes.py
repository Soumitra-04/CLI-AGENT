import datetime
def save_note(text):
    with open("memory/notes.txt","a") as file:
        now = datetime.datetime.now()
        date_today = now.strftime("%Y-%m-%d %H:%M")
        formatted = f"[{date_today}] {text}\n"
        file.write(formatted)
