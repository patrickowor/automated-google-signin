import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from xpaths import PATHS as paths
from target_urls import URL as urls


MUINITE = 60

driver = webdriver.Chrome()
wait = WebDriverWait(driver, MUINITE * 3)

def wait_for_correct_current_url(desired_url):
    wait.until(
        lambda driver: driver.current_url == desired_url)

def find_el(str, multi=False):
    if multi:
        return driver.find_elements(by=By.XPATH, value=str)
    return driver.find_element(by=By.XPATH, value=str)

def main(EMAIL, PASSWORD):
    driver.get(urls.start)
    wait_for_correct_current_url(urls.start)
    time.sleep(2)
    find_el(paths.signinButton).click()
    wait.until(lambda driver: driver.current_url.startswith(urls.accounts) ) # or  driver.current_url == url after login)
    find_el(paths.InputUsername).send_keys(EMAIL)
    find_el(paths.InputUserNamePageNextButton).click()
    wait.until(lambda driver: len(driver.find_elements(by=By.XPATH, value=paths.ShowPasswordText)) > 0 and find_el(paths.ShowPasswordText).text.strip() == "Show password")
    find_el(paths.InputUserPassword).send_keys(PASSWORD)
    find_el(paths.InputPasswordPageNextButton).click()
    print("in case of google pop up you can manually interact with them the script will wait here until you are done")
    wait.until(lambda driver: driver.current_url.startswith(urls.dashboard))

    print("login to google voice successful")


if __name__ == "__main__":
    EMAIL=input("Enter Your Email: ")
    PASSWORD=input("Enter Your Password: ")
    main(EMAIL, PASSWORD)