from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec 
import pytest

class Test_Sauce_Odev1:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window() 

    def teardown_method(self):
        self.driver.quit()
    
    @pytest.mark.parametrize("username,password",[("1","secret_sauce"),("problem_user","1"),("1","1")])
    def test_invalid_login(self,username,password):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys(username)
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys(password)
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"


    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")]) 
    def test_urun_ekle(self,username,password):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys(username)
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys(password)
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        addToCart = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='add-to-cart-sauce-labs-backpack']")))
        addToCart.click()
        shoppingCartLink = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='shopping_cart_container']/a")))
        shoppingCartLink.click()
        product = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='item_4_title_link']")))
        mesagge = product.text
        print(f"Sepetteki urun adı: {mesagge}")
        continueShopping = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='continue-shopping']")))
        continueShopping.click()
        remove = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*//*[@id='remove-sauce-labs-backpack']")))
        assert remove.text == "Remove"

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")]) 
    def test_urun_inceleme(self,username,password):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys(username)
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys(password)
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        self.driver.execute_script("window.scrollTo(0,500)")
        itemName= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='item_2_title_link']/div")))
        itemName.click()
        productTitle = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='inventory_item_container']/div/div/div[2]/div[1]")))
        message = productTitle.text
        print(f"Urunun Adi: {message}")
        backButton = self.driver.find_element(By.XPATH,"//*[@id='back-to-products']")
        backButton.click()
        assert message == "Sauce Labs Onesie"
