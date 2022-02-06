from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд
    #browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    #button = browser.find_element_by_id("verify")
    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Ваш код, который заполняет обязательные поля
    x = browser.find_element_by_id("input_value").text

    # Enter the answer
    answer_textbox = browser.find_element_by_id("answer")
    answer_textbox.send_keys(calc(x))

    button = browser.find_element_by_id("solve")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла