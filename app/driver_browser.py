
from selenium.common.exceptions import TimeoutException
from functions import get_platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



class DriverBrowser():
    
    def __init__(self):
        self.driver = None
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox");
        chrome_options.add_argument("--disable-dev-shm-usage");
            
        if get_platform() == 'OS X':
            self.driver = webdriver.Chrome(options=chrome_options)
        elif get_platform() == 'linux':
            self.driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", options=chrome_options)
            
    def get_elements_by_selector(self, url, selector):
        try:
            self.driver.get(url)
            elements = WebDriverWait(self.driver, 3).until(
                        EC.presence_of_all_elements_located((By.CLASS_NAME, selector))
                    )
            return elements
        except TimeoutException as e:
            raise(e)
        

    def close(self):
        self.driver.close()
        self.driver.quit()