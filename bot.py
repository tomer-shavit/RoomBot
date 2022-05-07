from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver


class RoomBot:
    def __init__(self, ID_list, user_email, user_password):
        self.user_email = user_email
        self.user_password = user_password
        self.ID_list = ID_list
        self.start_day = 0

    def login(self, driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'pills-email-tab'))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'username'))).send_keys(self.user_email)  # add email instead of empty string
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'password'))).send_keys(self.user_password)  # add password instead of empty string
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(., "Enter")]'))).click()

    def choose_library(self):
        driver = setup()
        driver.get('https://www.huji.ac.il/rooms/')
        driver.maximize_window()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'open_pop'))).click()

        self.login(driver)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[text()='בית הספר להנדסה ולמדעי המחשב']"))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'next'))).click()

        time.sleep(20)
        driver.close()

    def book_room(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.start_day = input("Please write the start date:\n")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        # driver = webdriver.Chrome(self.driver_address)
        driver.get('https://www.huji.ac.il/rooms/')
        library_check = driver.find_element(By.ID, "Computer")
        library_check.click()
        time.sleep(2000)
        library_next = driver.find_element(By.ID, "next")
        print(library_next.text)
        library_next.click()
        time.sleep(1000)
        date_button = driver.find_element(By.XPATH, f"//button[@day,'{self.start_day}')]")
        date_button.click()









