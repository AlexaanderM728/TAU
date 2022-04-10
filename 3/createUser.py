from selenium import webdriver
import time
import logging
# Main Function
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    logging.basicConfig(filename='test1.log', level=logging.INFO, format='%(asctime)s %(message)s')
    logger = logging.getLogger('task')
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')

    # Provide the path of chromedriver present on your system.
    driver = webdriver.Chrome(executable_path="chromedriver",
                              chrome_options=options)
    driver.set_window_size(1420, 900)

    # Send a get request to the url
    driver.get("https://www.morele.net/")
    logger.info("open website")
    time.sleep(4)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div/button').click()
    time.sleep(4)
    logger.info('Coockies accept button clicked')

    driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div/div/div[2]/div/div[2]/div/div[4]/a').click()
    logger.info('Create user button clicked')
    time.sleep(4)
    driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div[2]').click()
    logger.info('Start create user')
    time.sleep(4)
    input_email = driver.find_element(By.XPATH, '/html/body/main/div/div/div[4]/form/div[1]/input')
    input_email.send_keys('jakkowalski141990@gmail.com')
    logger.info('the email was entered')
    time.sleep(5)
    input_pass = driver.find_element(By.XPATH, '/html/body/main/div/div/div[4]/form/div[2]/input')
    input_pass.send_keys('!@acf@#ghhK29304')
    logger.info('the password was entered')
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/main/div/div/div[4]/form/div[3]/label/span[1]').click()
    time.sleep(3)
    logger.info('accepted by the regulations')
    driver.find_element(By.XPATH, '/html/body/main/div/div/div[4]/form/button').click()
    time.sleep(3)
    logger.info("popup newsletter show")
    driver.find_element(By.XPATH, '/html/body/main/div/div/div[4]/form/button').click()
    logger.info('account created')
    time.sleep(60)
    driver.quit()
    print("Done")

