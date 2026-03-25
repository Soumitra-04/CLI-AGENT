import pywhatkit
import datetime
# Syntax: sendwhatmsg(phone_no, message, time_hour, time_min)
def whatsapp(phone_number,message):
    curr_time= datetime.datetime.now() + datetime.timedelta(minutes=1)
    hour = curr_time.hour
    minute = curr_time.minute
    try:
        print("Sending message...\n")
        pywhatkit.sendwhatmsg(phone_number, message, hour, minute,wait_time=15)
        return "Message sent Successfully"
    except Exception as e:
        return e