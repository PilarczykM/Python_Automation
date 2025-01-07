from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.thesun.co.uk/sport/football/"

options = Options()
# options.add_argument("--headless")

chrome = webdriver.Chrome(options=options)
chrome.get(URL)

# Wrapper for dynamic content
chrome_wait = WebDriverWait(chrome, 3)

try:
    accept_cookie_button = chrome_wait.until(
        EC.presence_of_all_elements_located((By.XPATH, "//button[contains(@title, 'Accept')]")), "Accept button not found")
except Exception as e:
    print(e)

try:
    articles_content = "//div[contains(@class, 'teaser__copy-container')]"
    articles = chrome_wait.until(
        EC.presence_of_all_elements_located((By.XPATH, articles_content)), "Articles not found")
    
    articles_content_titles =  "./a/h3"
    for article in articles:
        try:
            title_element = article.find_element(By.XPATH, articles_content_titles)
            title_content = title_element.accessible_name
            print("Title: " + title_content)
        except Exception as e:
            print(f"Error: {e.msg}")
    pass
except Exception as e:
    print(e)



chrome.close()