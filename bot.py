from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class RoomBot:
    def __init__(self, ID_list, user_email, user_password):
        self.user_email = user_email
        self.user_password = user_password
        self.ID_list = ID_list
        self.start_day = 0

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









