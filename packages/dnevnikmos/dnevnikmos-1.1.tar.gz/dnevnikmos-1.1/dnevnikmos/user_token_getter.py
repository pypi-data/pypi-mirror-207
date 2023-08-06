from selenium import webdriver
from time import time, sleep
from urllib3.util import parse_url
from selenium.webdriver.common.by import By
from sys import exit



class UserToken:
    def get_token(login, password, executable_path):
        start_time = time()
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(options=options, executable_path=executable_path)
        driver.get("https://school.mos.ru")
        sleep(3)
        login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/main/section/div/div[1]/div[3]/div/div[1]/div[2]/div')
        login_button.click()
        sleep(5)
        login_input = driver.find_element(By.ID, "login")
        login_input.send_keys(login)
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys(password)
        submit_button = driver.find_element(By.ID, "bind")
        submit_button.click()
        while "/?token" not in driver.current_url:
            pass
        try:
            callback_code = parse_url(driver.current_url).query[6:-17]
        except TypeError:
            driver.close()
            return "Возникла ошибка"

        driver.close()

        return callback_code
