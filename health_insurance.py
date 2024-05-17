from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.chrome.options import Options
import time
from config_url import BASE_URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opt = Options()
# driver = webdriver.Chrome(service=s, options=opt)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("log-level=3")
driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome(opt)
driver.get(BASE_URL)
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//button[@class='text-sm lg:text-xs bg-theme-blue w-5 h-5 px-1 rounded-full text-white btn-cookie fixed bottom-8 -right-1 md:bottom-4 mr-2 md:mr-0']").click()
driver.find_element(By.XPATH,"//a[text()='Services']").click()
driver.find_element(By.XPATH,"//div[text()='Explore All Services']").click()
driver.find_element(By.XPATH,"(//p[text()='Health Insurance - OSHC'])[2]").click()
driver.find_element(By.XPATH,"//option[text()='Select Country']").click()
driver.find_element(By.XPATH,"//option[text()='Australia']").click()
driver.find_element(By.XPATH,"//div[text()='Book Now']").click()
driver.find_element(By.XPATH,"//input[@placeholder='Enter Email']").send_keys("pravin.garg@universityliving.com")
driver.find_element(By.XPATH,"//div[text()='Login']").click()

driver.find_element(By.NAME, "otp0").send_keys("5")
driver.find_element(By.NAME, "otp1").send_keys("4")
driver.find_element(By.NAME, "otp2").send_keys("3")
driver.find_element(By.NAME, "otp3").send_keys("2")
driver.find_element(By.NAME, "otp4").send_keys("1")
driver.find_element(By.CSS_SELECTOR, "form button div").click()
driver.find_element(By.XPATH,"//div[text()='Book Now']").click()
driver.find_element(By.XPATH,"//option[text()='Select number of children']").click()
driver.find_element(By.XPATH,"//input[@placeholder='Start Date']").click()
driver.find_element(By.XPATH,"(//td[text()='30'])[2]").click()
driver.find_element(By.XPATH,"(//button[@type='button'])[3]").click()
driver.find_element(By.XPATH,"(//div[@role='button'])[3]").click()
driver.find_element(By.XPATH,"(//td[text()='30'])[2]").click()
driver.find_element(By.XPATH,"//div[text()='Submit']").click()
time.sleep(10)
driver.quit()
