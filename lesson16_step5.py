# Это тестовое задание
# Строка описания
import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
browser = webdriver.Chrome("C://Локальные документы//chromedriver.exe")
link = "http://suninjuly.github.io/registration2.html"


try:
    browser.get(link)

    input1 = browser.find_element_by_xpath("//label[text()='First name*']/following-sibling::input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//label[text()='Last name*']/following-sibling::input")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("//label[text()='Email*']/following-sibling::input")
    input3.send_keys("1@1.ru")
    input4 = browser.find_element_by_xpath("//label[text()='Phone:']/following-sibling::input")
    input4.send_keys("8902456789")
    input4 = browser.find_element_by_xpath("//label[text()='Address:']/following-sibling::input")
    input4.send_keys("г.Москва")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

# Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла