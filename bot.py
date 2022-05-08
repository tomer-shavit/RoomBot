from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
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

        # Choosing the log by email option
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'pills-email-tab'))).click()

        # Now entering email character by character
        for char in self.user_email:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'username'))).send_keys(char)
            time.sleep(0.3)

        time.sleep(3)

        # Now entering password character by character
        for char in self.user_password:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'password'))).send_keys(char)
            time.sleep(0.3)

        time.sleep(2)

        # Now login
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(., "Enter")]'))).click()

    def open_website(self):

        # Open website
        self.driver.get('https://www.huji.ac.il/rooms/')
        self.driver.maximize_window()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'open_pop'))).click()

    def choose_library(self):
        self.open_website()
        self.login()

        # Choose the library and proceed the order
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[text()='בית הספר להנדסה ולמדעי המחשב']"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'next'))).click()

    def choose_date(self):

        # Choose the date of order
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@day='12']"))).click()

    def choose_rooms(self):

        # Choose room 1
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='14,121']"))).click()

        # Choose room 2
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='15,121']"))).click()

        # Choose room 3
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='16,121']"))).click()

        # Proceed the booking to the id's stage
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'next1'))).click()

    def enter_ids(self):

        # Entering first id
        time.sleep(3)
        for digit in self.id_list[6]:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'zehut1'))).send_keys(digit)
            time.sleep(0.3)

        # Validating id
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//font[text()='ליחצו כאן לאימות ת.ז.']"))).click()

        # Entering second id
        time.sleep(3)
        for digit in self.id_list[10]:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'zehut2'))).send_keys(digit)
            time.sleep(0.3)

        # Validating id
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//font[text()='ליחצו כאן לאימות ת.ז.']"))).click()

        # Finnish booking the room
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'next'))).click()

    def run(self):
        self.choose_library()
        self.choose_date()
        self.choose_rooms()
        self.enter_ids()
