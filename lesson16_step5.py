# ��� �������� �������
# ������ ��������
import time

# webdriver ��� � ���� ����� ������ ��� ���������� ���������
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

# �������������� ������� ��������. ����� ���� ������� �� ������ ������� ����� �������� ���� ��������
browser = webdriver.Chrome("C://��������� ���������//chromedriver.exe")
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
    input4.send_keys("�.������")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

# ���������, ��� ������ ������������������
    # ���� �������� ��������
    time.sleep(1)

    # ������� �������, ���������� �����
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # ���������� � ���������� welcome_text ����� �� �������� welcome_text_elt
    welcome_text = welcome_text_elt.text

    # � ������� assert ���������, ��� ��������� ����� ��������� � ������� �� �������� �����
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # �������� ����������� ��� �� 30 ������
    time.sleep(5)
    # ��������� ������� ����� ���� �����������
    browser.quit()

# �� �������� �������� ������ ������ � ����� �����