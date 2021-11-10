from selenium import webdriver

from user_env import my_love

browser = webdriver.Chrome(executable_path='./chromedriver')
browser.get(url=my_love.get("url"))

browser.close()
