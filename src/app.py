import os
from time import sleep
from slack_sdk import WebClient
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

EMAIL = 'xxx@icloud.com'
PASSWORD = 'xxx'
SLACK_TOKEN = "xoxb-foo"
SLACK_CHANNEL_ID = "Cxxx"


def get_driver():
    return webdriver.Remote(
        command_executor=os.environ["SELENIUM_URL"],
        desired_capabilities=DesiredCapabilities.CHROME.copy()
    )


def login(driver):
    driver.get('https://xxx.com')
    driver.find_elements_by_css_selector('input[type="email"]')[0]\
        .send_keys(EMAIL)
    driver.find_elements_by_css_selector('input[type="password"]')[0]\
        .send_keys(PASSWORD)
    driver.find_element_by_id('signIn').click()


def notify(driver, file_path: str):
    client = WebClient(token=SLACK_TOKEN)
    client.files_upload(
        channels=SLACK_CHANNEL_ID,
        initial_comment="Screenshot :smile:",
        file=file_path,
    )


def lambda_handler(event, context):
    try:
        driver = get_driver()
        driver.implicitly_wait(5)
        login(driver)
    except Exception as e:
        raise e
    finally:
        sleep(5)
        path = "/tmp/result.png"
        driver.save_screenshot(path)
        notify(driver, path)
        driver.quit()


if __name__ == '__main__':
    lambda_handler(None, None)
