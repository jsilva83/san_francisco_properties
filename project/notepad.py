from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

URL_TO_WEBSCRAP = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22' \
                  'usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-' \
                  '122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22is' \
                  'MapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%' \
                  '7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afa' \
                  'lse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%' \
                  '22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22' \
                  '%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds' \
                  '%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'

a_service = Service(ChromeDriverManager().install())
a_options = Options()
# a_options.add_argument("--headless")
a_options.add_argument("window-size=1400,1000")
a_driver = webdriver.Chrome(service=a_service, options=a_options)
a_driver.get(url=URL_TO_WEBSCRAP)

# last_height = a_driver.execute_script("return document.body.scrollHeight")
# a_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# ul_element = a_driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/div/div[1]/div[1]/ul')
# a_driver.execute_script("arguments[0].scrollIntoView(true);", ul_element)
# a_driver.execute_script("arguments[0].scrollIntoView(true);", ul_element)

# ul_element.send_keys(Keys.PAGE_DOWN)
# ul_element.send_Keys(Keys.PAGE_DOWN)


a_driver.execute_script('window.scrollBy(800, document.body.scrollHeight);')
a_driver.execute_script('window.scrollBy(800, document.body.scrollHeight);')
