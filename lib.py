import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import requests
from requests.structures import CaseInsensitiveDict
import ast
from encodings import utf_8


def loginCookie(driver):
    driver.get('https://elearning-ability.tdtu.edu.vn/')
    f = open("cookies.json")
    cookies = json.load(f)
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


def write_key(key):
    f = open('keypy.json', 'w', encoding='utf-8')
    f.write(json.dumps(key))
    f.close()


def post_key(key):
    url = "https://key.trongtinh7727.repl.co/api/post/"
    print(requests.post(url + key).content)


def get_key():
    url = "https://key.trongtinh7727.repl.co/api/getkey"
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    resp = requests.get(url, headers=headers)
    byte_str = resp.content
    dict_str = byte_str.decode("UTF-8")
    key = ast.literal_eval(dict_str)
    return key


def answered(driver, number, key):
    for i in range(1, number):
        title_input = WebDriverWait(driver, 100).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "#List-Question")))
        time.sleep(1)
        ques = driver.find_element(
            By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[1]/div['+str(i)+']/div/p').text

        for ans_num in range(1, 5):
            answer = driver.find_element(
                By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[1]/div['+str(i)+']/ul/li['+str(ans_num)+']').text
            if answer == key[ques]:
                case = driver.find_element(
                    By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[1]/div['+str(i)+']/ul/li['+str(ans_num)+']/div[1]/div/ins').click()
            else:
                continue


def sloveQ(driver, number, ques, quiz_url, key, doc):
    title_input = WebDriverWait(driver, 100).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, "#List-Question")))
    time.sleep(1)
    # lay dap an
    for n in range(1, 5):

        answer = driver.find_element(
            By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[1]/div['+str(number)+']/ul/li['+str(n)+']').text
        if not (answer in doc):
            doc[answer] = ""
            driver.find_element(
                By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[1]/div['+str(number)+']/ul/li['+str(n)+']/div[1]/div/ins').click()
            break
    print("temp_ans: "+answer)
    answered(driver, number, key)
    driver.find_element(By.ID, 'btnNext').click()
    title_input = WebDriverWait(driver, 100).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, "#btnSubmitAndFinish")))
    driver.execute_script(open("./cormfim.js", encoding='utf-8').read())
    driver.find_element(By.ID, 'btnSubmitAndFinish').click()
    driver.get(quiz_url)

    score = driver.find_elements(
        By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[2]/div[2]/div/div/table/tbody/tr')
    print("Score: "+str(len(score)))
    score = driver.find_element(
        By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[2]/div[2]/div/div/table/tbody/tr['+str(len(score))+']/td[6]').text
    if int(score) == number:
        key[ques] = answer
        print("Done: "+ques)
        post_key(ques+"_"+answer)
        write_key(key)
        return True
    else:
        return sloveQ(driver, number, ques, quiz_url, key, doc)


def auto_quizz(driver, quiz_url):
    # f = open('keypy.json', encoding='utf-8')
    # key = json.load(f)
    # f.close()

    doc = {}
    key = get_key()

    driver.get(quiz_url)
    title_input = WebDriverWait(driver, 100).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, "#timer")))

    a = driver.find_elements(
        By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[1]/div')

    total = len(a)
    print(total)

    for i in range(1, total+1):
        title_input = WebDriverWait(driver, 100).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "#List-Question")))
        time.sleep(3)

        ques = driver.find_element(
            By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[1]/div['+str(i)+']/div/p').text
        print("Ques: " + ques)
        try:
            print(key[ques])
            for ans_num in range(1, 5):
                answer = driver.find_element(
                    By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[1]/div['+str(i)+']/ul/li['+str(ans_num)+']').text
                if answer == key[ques]:
                    case = driver.find_element(
                        By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[1]/div['+str(i)+']/ul/li['+str(ans_num)+']/div[1]/div/ins').click()
                else:
                    continue
            print("Done cau "+str(i))
        except:
            print("Start slove.....")
            sloveQ(driver, i, ques, quiz_url, key, doc)


def lessonSkip(driver):
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


def get_lesson(driver, class_url):
    driver.get(class_url)
    list_lesson = driver.find_elements(
        By.XPATH, '//*[@id="ListLesson"]/li')
    total = len(list_lesson)
    print(total)

    for i in range(1, total+1):
        try:
            span = driver.find_element(
                By.XPATH, '//*[@id="ListLesson"]/li['+str(i)+']/span')
        except:
            a = driver.find_element(
                By.XPATH, '//*[@id="ListLesson"]/li['+str(i)+']/a').click()
            lessonSkip(driver)
            quiz_url = driver.current_url
            print(quiz_url)
            auto_quizz(driver, quiz_url)
            return total - i
