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
    def __init__(self, id_list, user_email, user_password, day):
        self.driver = setup()
        self.user_email = user_email
        self.user_password = user_password
        self.id_list = id_list
        self.day = day

    def login(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'pills-email-tab'))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'username'))).send_keys(self.user_email)  # add email instead of empty string
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'password'))).send_keys(self.user_password)  # add password instead of empty string
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(., "Enter")]'))).click()

    def open_website(self):
        self.driver.get('https://www.huji.ac.il/rooms/')
        self.driver.maximize_window()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'open_pop'))).click()

    def choose_library(self):
        self.open_website()
        self.login()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[text()='בית הספר להנדסה ולמדעי המחשב']"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'next'))).click()

    def choose_date(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@day='12']"))).click()

    def choose_rooms(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//checkbox[@value='14,121']"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//checkbox[@value='15,121']"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//checkbox[@value='16,121']"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@text()='המשך']"))).click()

    def enter_ids(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'zehut1'))).send_keys(self.id_list[6])
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//font[text()='ליחצו כאן לאימות ת.ז.']"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'zehut2'))).send_keys(self.id_list[6])
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//font[text()='ליחצו כאן לאימות ת.ז.']"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@text()='המשך']"))).click()

    def run(self):
        self.choose_library()
        self.choose_date()
        self.choose_rooms()
        self.enter_ids()
        time.sleep(100)

