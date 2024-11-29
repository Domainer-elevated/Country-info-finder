from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Setup Chrome options for headless mode
options = Options()
options.add_argument("--headless")  # Headless mode
options.add_argument("--no-sandbox")  # Disable sandboxing (required for Linux)
options.add_argument("--disable-dev-shm-usage")  # Prevent issues with shared memory

# Specify the ChromeDriver location
service = Service("/usr/local/bin/chromedriver")

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://cosmocode.io/automation-practice-webtable/")
driver.maximize_window()
table = driver.find_element(By.ID, 'countries')
rows = table.find_elements(By.TAG_NAME, 'tr')

def get_currency(name):
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        if name in cells[1].text:
            return cells[3].text

def get_capital(name):
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        if name in cells[1].text:
            return cells[2].text

def get_language(name):
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        if name in cells[1].text:
            return cells[4].text

def main():
    coutnry = 'Albania'
    capital = get_capital(coutnry)
    currency = get_currency(coutnry)
    lang = get_language(coutnry)
    print(capital)
    print(currency)
    print(lang)
if __name__ == '__main__':
    main()



