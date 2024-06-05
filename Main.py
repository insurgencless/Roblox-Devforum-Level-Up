from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
import random

driver = webdriver.Chrome()
driver.get("https://roblox.com")

def Auto_Scroll():
    actions = ActionChains(driver)
    sleep(3)
    Domain = f"https://devforum.roblox.com/t/2916442"
    driver.get(Domain)
    sleep(6)
    while True: 
        Selected_Name = 0
        try:
            Selected_Element = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "trigger-user-card.main-avatar")))
        except:
            print("error")
        else:
            for element in Selected_Element:
                if Selected_Name >= 4:
                    sleep(10)
                    actions.move_to_element(element).perform()
                    print("SCROLLED")
                    Selected_Name +=1
        sleep(15)
        elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "title.raw-link.raw-topic-link"))
        )
        if elements:
            random.choice(elements).click()
        sleep(4)
            
            
def Main():
    driver.execute_script(f"""
                var RobloxCookie = '.ROBLOSECURITY';
                var CookieValue =  '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-wil PUT COOKIE HERE';
                var MyDate = new Date();
                MyDate.setMonth(MyDate.getMonth() + 12);
                document.cookie = RobloxCookie + "=" + CookieValue + ";expires=" + MyDate + ";domain=.roblox.com;path=/"
                setTimeout(() => {{
                    location.reload();
                }}, 2500);
                """)
    driver.get("https://devforum.roblox.com/")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "widget-button.btn.btn-primary.btn-small.login-button.btn-icon-text"))).click()
    sleep(4)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button']"))).click()
    print("clicked")

while True:
    try:
        Main()
        Auto_Scroll()
    except:
        driver.quit()
        driver.get("https://roblox.com")
