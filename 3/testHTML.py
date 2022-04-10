import runpy
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
import createUser

class TestDriver():

    @pytest.fixture()
    def setup(self):
        global driver
        self.driver = webdriver.Chrome(executable_path="chromedriver")
        self.driver.maximize_window()
        yield
        self.driver.close()


    @pytest.fixture()
    def setulogin(self):
        global driver
        runpy.run_path(run_name=createUser.py)
        self.driver = webdriver.Chrome(executable_path="chromedriver")
        self.driver.set_window_size(1420, 900)
        yield


    def test_PageTitle(self, setup):
        self.driver.get("https://www.morele.net/login")
        assert self.driver.title == "Sklep komputerowy Morele.net"

    def test_create_user(self, setulogin):
        self.driver.get("https://www.morele.net/login")
        self.WebDriverWait(driver, 10)
        self.driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div[2]').click()
        self.driver.find_element(By.XPATH, '/html/body/main/div/div/div[4]/form/div[1]/input').send_keys('jakkowalski141990@gmail.com')
        self.driver.find_element(By.XPATH, '/html/body/main/div/div/div[4]/form/div[2]/input').send_keys('!@acf@#ghhK29304')
        self.driver.find_element(By.XPATH, '/html/body/main/div/div/div[4]/form/div[3]/label/span[1]/span/span/span[2]').click()
        self.driver.find_element(By.XPATH, '/html/body/main/div/div/div[4]/form/div[4]/div[1]/label/span[1]/span/span/span[2]').click()
        self.driver.find_element(By.XPATH, '/html/body/main/div/div/div[4]/form/button').click()
        self.WebDriverWait(driver, 10)
        self.driver.close()
        assert self.driver.title == "Morele - zakupy online to pestka"

    def test_login(self, setulogin):
        self.driver.get("https://www.morele.net/login")
        self.driver.find_element(By.XPATH, '/html/body/main/div/div/div[3]/form/div[1]/input').send_keys('jakkowalski141990@gmail.com')
        self.driver.find_element(By.XPATH, '/html/body/main/div/div/div[3]/form/div[2]/input').send_keys('!@acf@#ghhK29304')
        self.driver.find_element(By.XPATH, '/html/body/main/div/div/div[3]/form/button').click()
        self.driver.close()
        assert self.driver.title == "Morele - zakupy online to pestka"

    def test_delete_user(self, setup):
        self.driver.get('https://www.morele.net/profil/')
        main_page = self.driver.current_window_handle
        self.driver.find_element(By.XPATH, '/html/body/div[3]/section/section/div[2]/div[1]/div[1]/nav/ul/li[3]/a').click()
        self.driver.find_element(By.XPATH, '/html/body/div[3]/section/section/div[2]/div[3]/a').click()
        for handle in driver.window_handles:
            if handle != main_page:
                login_page = handle

        driver.switch_to.window(login_page)
        self.time.sleep(5)
        self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]').click()
        driver.switch_to.window(main_page)
        self.time.sleep(4)
        assert self.driver.title == "Sklep komputerowy Morele.net"


