from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.chrome.options import Options
import time

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
driver.get("https://universityliving.com")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//button[@class='text-sm lg:text-xs bg-theme-blue w-5 h-5 px-1 rounded-full text-white btn-cookie fixed bottom-8 -right-1 md:bottom-4 mr-2 md:mr-0']").click()
driver.find_element(By.XPATH,"//a[text()='Services']").click()
driver.find_element(By.XPATH,"//div[text()='Explore All Services']").click()
driver.find_element(By.XPATH,"//p[@class='te-listing-ap text-theme-blue content-font md:text-base font-bold md:font-semibold flex items-center mb-2 gap-2']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Jayride']").click()
driver.find_element(By.XPATH,"//div[text()='Find a Pickup']").click()
driver.find_element(By.XPATH,"//input[@placeholder='Enter Email']").send_keys("pravin.garg@universityliving.com")
driver.find_element(By.XPATH,"//div[text()='Login']").click()

driver.find_element(By.NAME, "otp0").send_keys("5")
driver.find_element(By.NAME, "otp1").send_keys("4")
driver.find_element(By.NAME, "otp2").send_keys("3")
driver.find_element(By.NAME, "otp3").send_keys("2")
driver.find_element(By.NAME, "otp4").send_keys("1")
driver.find_element(By.CSS_SELECTOR, "form button div").click()
driver.find_element(By.XPATH,"//div[text()='Find a Pickup']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("test")
driver.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("testing")
driver.find_element(By.XPATH,"//input[@placeholder='Email']").send_keys("pravin.garg@universityliving.com")
driver.find_element(By.XPATH,"//input[@placeholder='Contact Number']").send_keys("9012659233")
driver.find_element(By.XPATH,"//div[text()='Submit']").click()
time.sleep(10)
driver.quit()
