import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from wa_automate import WAProtocol, WAConnection

chrome_options = Options()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

# Load session from file
wa = WAConnection()
wa.load_from_file('session.json')

# Inject session into browser
driver.get('https://web.whatsapp.com/')
wa.browser = driver

# Wait for login
wa.wait_for_login()

while True:
    message = wa.listen_messages()
    if ".gn" in message.text.lower():
        driver.get("https://web.whatsapp.com/send?phone=" + message.chat_id + "&text=good%20night")

