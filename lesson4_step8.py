from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return math.log(abs(12*math.sin(x)))

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    book_button = browser.find_element(By.ID, 'book')
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    book_button.click()

    x_element = browser.find_element(By.ID, 'input_value')
    x = int(x_element.text)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(calc(x))

    submit_button = browser.find_element(By.ID, 'solve')
    submit_button.click()
finally:
    time.sleep(10)
    browser.quit()

