from selenium import webdriver
import time
import logging
import sys
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
    logger.info("Test guzika akceptuj cookie, wyszukiwania produktu na stronie ceneo.pl wraz z filtrem ofert")
    driver.get('https://www.ceneo.pl')
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, 'btn.btn-info.btn-origin.js_cookie-monster-agree.js_gtm_button').click()
    driver.switch_to.default_content()
    logger.info("Znalesiono button Akceptuj cookie")
    time.sleep(3)

    logger.info('akcepotowano polityke cookie')
    driver.find_element(By.NAME, 'search-query').click()
    logger.info('znaleziono wyszukiwarke strony')
    input_1 = driver.find_element(By.ID, 'form-head-search-q')
    input_1.send_keys("iphone 13 pro")
    logger.info('wpisano fraze')
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'header-search__button__text').click()
    logger.info('kliknieto guzik szukaj')
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[@title='Apple iPhone 13 Pro 128GB Mocny Grafit']").click()
    logger.info("znaleziono szukany element po atrybucie title")
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div/div/div[1]/div[5]/div[2]/div[1]/div/div/div[1]/a/b').click()
    logger.info("kliknieto sortowanie według")
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div/div/div[1]/div[5]/div[2]/div[1]/div/div/div[1]/div/a[4]').click()
    logger.info("wybrano sorotwaniu według najwyzsza cena z dostawą")
    logger.info("Koniec")
    time.sleep(10)
    driver.quit()
    print("Done")

