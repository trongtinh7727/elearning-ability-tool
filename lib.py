import pickle
import pprint
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


def loginCookie(driver, cookies):
    driver.get('https://elearning-ability.tdtu.edu.vn/')
    # f = open("cookies.json")
    cookies = json.loads(cookies)
    cookies = cookies['cookies']

    for cookie in cookies:
        cookie['sameSite'] = 'Lax'
        driver.add_cookie(cookie)
    driver.get('https://elearning-ability.tdtu.edu.vn/')


def login(driver, user, pwd):
    driver.get('https://elearning-ability.tdtu.edu.vn/')
    login = ("document.querySelector('#login_button').click()", "document.querySelector('input[name=\"UserID\"]').value = "+user,
             "document.querySelector('input[name=\"UserPassword\"]').value = "+pwd, "document.querySelector('#btnLogin').click()")
    for i in login:
        driver.execute_script(i)
    title_input = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, "#content-warning")))


def Next(driver):
    try:
        driver.find_element(By.ID, "btnNext").click()
    except:
        return False
    return True


def finish(driver):
    try:
        driver.find_element(By.ID, "btnFinish").click()
    except:
        return False
    return True


def lessonSkip(driver, class_ulr):
    driver.get(class_ulr)
    time.sleep(5)
    Next(driver)
    lis = driver.find_elements(By.XPATH, '//li')

    for n in lis:
        try:
            test = driver.find_element(
                By.XPATH, '//*[@id="educo_wrapper"]/div[1]/div/div/div/div[2]/div[2]/div/form/div[2]/button')
            break
        except:
            print(0)
            time.sleep(1)
            if not Next(driver):
                finish(driver)
