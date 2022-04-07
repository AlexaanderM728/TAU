from selenium import webdriver
import logging
import time


# Main Function
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    logging.basicConfig(filename='test2.log', level=logging.INFO, format='%(asctime)s %(message)s')
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
    logger.info("Test akceptacji pliku cookie, wyszukiwarki morele.net i próba zalogowania do serwisu. Oczekiwany rezultat: strona doda produkt do koszyka i nie odnajdzie uzytkownia o emialu :user1@mail.com.")
    driver.get('https://www.morele.net/')
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, 'btn.btn-secondary.btn-secondary-outline.btn-md.close-cookie-box').click()
    driver.switch_to.default_content()
    logger.info("Znalesiono button Akceptuj cookie")
    time.sleep(3)
    logger.info('akcepotowano polityke cookie')
    driver.find_element(By.NAME, 'search').click()
    logger.info('znaleziono wyszukiwarke strony')
    input_1 = driver.find_element(By.CLASS_NAME, 'form-control.quick-search-autocomplete')
    input_1.send_keys("xbox")
    logger.info('wpisano fraze')
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'btn.btn-primary.h-quick-search-submit').click()
    logger.info('kliknieto guzik szukaj')
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div[2]/div/div[6]/div[1]/div[2]/div/div[2]/div[1]/div/p/a").click()
    logger.info("znaleziono szukany element po atrybucie title")
    driver.find_element(By.XPATH, "/html/body/main/div/section/div[1]/div[7]/aside/div[1]/div[4]/div[3]/div[1]/a").click()
    logger.info("Kliknieto dodaj do koszyka")
    time.sleep(3)

    for x in range(1, 2):
        while True:
            try:
                driver.find_element(By.XPATH, '//*[@id="catalog_product"]/div[10]/div/div/div[2]/div[1]/button/i').click()
                logger.info("wybrano guzik 'X'")
                time.sleep(1)
            except:
                    continue
            else:
                logger.warning("nie znaleziono elementu")
                time.sleep(1)
                driver.find_element(By.XPATH, '/html/body/main/div/section/div[1]/div[7]/aside/div[1]/div[4]/div[3]/div[1]/a')
                logger.info("wybrano ZOBACZ KOSZYK")
                continue
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[6]/div/div/span[2]/a')
    logger.info("wybrano guzik 'Do koszyka'")
    driver.find_element(By.CLASS_NAME, "confirm-button.btn.btn-primary.btn-block").click()
    logger.info("Kliknieto 'Wybierz dostawę i płatność'")
    time.sleep(3)
    username = driver.find_element(By.NAME, "_username")
    password = driver.find_element(By.NAME, "_password")
    username.send_keys("user1@mail.com")
    logger.info("wpisano emial")
    password.send_keys("password")
    logger.info("wpisano haslo")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div[2]/div/div[1]/div[1]/form/button").click()
    logger.info("kliknieto zaloguj się")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[2]")
    logger.info("Strona wyświetliła komunikat o błedynch danych logowania")
    logger.info("test zaliczony!")
    time.sleep(2)
    driver.quit()
    print("Done")


