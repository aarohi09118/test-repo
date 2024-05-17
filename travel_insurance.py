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
driver.find_element(By.XPATH,"(//p[text()='Travel Insurance'])[2]").click()
driver.find_element(By.XPATH,"//div[text()='Book Now']").click()
driver.find_element(By.XPATH,"//option[text()='Select Travel Country']").click()
driver.find_element(By.XPATH,"//option[text()='Ireland']").click()
driver.find_element(By.XPATH,"//option[text()='Select Plan Type']").click()
driver.find_element(By.XPATH,"//option[text()='Worldwide Excluding USA/Canada']").click()
driver.find_element(By.ID,"travelStartDate").click()
driver.find_element(By.XPATH,"//td[text()='31']").click()
driver.find_element(By.ID,"travelEndDate").click()
time.sleep(5)
driver.find_element(By.XPATH,"(//div[@role='button'])[2]").click()
driver.find_element(By.XPATH,"(//td[text()='30'])[2]").click()
driver.find_element(By.ID,"dob").click()
driver.find_element(By.XPATH,"(//td[text()='11'])[2]").click()
driver.find_element(By.XPATH,"//div[text()='Get Quote']").click()
driver.find_element(By.XPATH,"(//div[text()='Buy Plan'])[1]").click()
driver.find_element(By.XPATH,"//input[@placeholder='Enter Email']").send_keys("pravin.garg@universityliving.com")
driver.find_element(By.XPATH,"//div[text()='Login']").click()
driver.find_element(By.NAME, "otp0").send_keys("5")
driver.find_element(By.NAME, "otp1").send_keys("4")
driver.find_element(By.NAME, "otp2").send_keys("3")
driver.find_element(By.NAME, "otp3").send_keys("2")
driver.find_element(By.NAME, "otp4").send_keys("1")
driver.find_element(By.CSS_SELECTOR, "form button div").click()
driver.find_element(By.XPATH,"(//div[text()='Buy Plan'])[1]").click()
driver.find_element(By.XPATH,"//option[text()='Title']").click()
driver.find_element(By.XPATH,"//option[text()='Ms']").click()
driver.find_element(By.XPATH,"//input[@placeholder='Passport']").send_keys("testing")
driver.find_element(By.XPATH,"//input[@placeholder='City']").send_keys("noida")
driver.find_element(By.XPATH,"//input[@placeholder='Address']").send_keys("noida")
driver.find_element(By.XPATH,"//input[@placeholder='Postal Code']").send_keys("201303")
driver.find_element(By.XPATH,"//input[@placeholder='Nominee']").send_keys("test")
driver.find_element(By.XPATH,"//select[@name='relationship']").click()
driver.find_element(By.XPATH,"//option[text()='Father']").click()
driver.find_element(By.XPATH,"//div[text()='Next']").click()
driver.find_element(By.XPATH,"//div[@class='flex items-center ']").click()
driver.find_element(By.XPATH,"//div[text()='Make Payment']").click()
time.sleep(10)
driver.quit()








