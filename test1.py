from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.implicitly_wait(5)
# assert "Internships" in driver.title
job = driver.find_element(By.ID, "bigCookie")
count = driver.find_element(By.ID, "cookies")
# elem.send_keys('pycon')
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
action = ActionChains(driver)
action.click()

for i in range(0, 100):
    action.perform()

sleep(10)
driver.close()