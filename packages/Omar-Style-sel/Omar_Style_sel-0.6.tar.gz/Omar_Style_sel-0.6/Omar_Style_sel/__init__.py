"""
Copyright: You are prohibited from publishing this project in another project
Code developer Omar_Style_ps

Contact for inquiries:
    https://t.me/OmarStyle1
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from time import sleep 

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#Omar_Style 
class BrowsersProxy:
    #Omar_Style 
    def proxy_firefox(self, pr, firr):
        try:
            proxy_host, proxy_port = pr.split(":")
            # print(proxy_host,proxy_port)
        except ValueError:
            print("Please enter the proxy correctly   Example  => 95.56.254.139:3128")
            return

        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("network.proxy.type", 1)
        firefox_profile.set_preference("network.proxy.http", proxy_host)
        firefox_profile.set_preference("network.proxy.http_port", int(proxy_port))
        firefox_profile.set_preference("network.proxy.ssl", proxy_host)
        firefox_profile.set_preference("network.proxy.ssl_port", int(proxy_port))

        driver = webdriver.Firefox(firefox_profile=firefox_profile)
        driver.get(firr)
        return driver

    def proxy_chrome(self,proxy_address,Link,user,driver_path=None):
        options = Options()
        # options.add_argument("window-size=1400,600")
        from fake_useragent import UserAgent
        ua = UserAgent()
        user_agent = ua.random
        # print(user_agent)
        if user:
            options.add_argument(f'user-agent={user_agent}')
            
        
        # driver = webdriver.Chrome(chrome_options=options)
        # driver.get('https://whoer.net/')
        # driver.quit()

        """

        Copyright: You are prohibited from publishing this project in another project
            Code developer Omar_Style_ps

        Contact for inquiries:
            https://t.me/OmarStyle1
        """
        try:
            proxy_host, proxy_port = proxy_address.split(":")
        except ValueError:
            raise ValueError("Please enter the proxy correctly. Example: 95.56.254.139:3128")

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f'--proxy-server={proxy_host}:{proxy_port}')

        if driver_path is None:
            driver = webdriver.Chrome(options=chrome_options)
        else:
            driver = webdriver.Chrome(driver_path, options=chrome_options)
        driver.get(Link)
        return driver



class Browsers:
    def firefox_b(url):
        firefox_profile = webdriver.FirefoxProfile()
        driver = webdriver.Firefox(firefox_profile=firefox_profile)
        driver.get(url)
        return driver
    def chrome_b(url,driver_path=None):
        options = Options()
        chrome_options = webdriver.ChromeOptions()
    
        # print(driver_path)
        if driver_path is None:
            driver = webdriver.Chrome(options=chrome_options)
            # print("Rul ")
        else:
            driver = webdriver.Chrome(driver_path, options=chrome_options)
            # print("EEEEEEEEEEEEEEEEEE ")
        driver.get(url)
        return driver


    def input_a(driver,kind,search,inp,successfully,error_message):
        pass
     
        while True:
            try:
                WebDriverWait(driver, 50).until(lambda driver: driver.find_element(kind, search)).send_keys(Keys.CONTROL+"a",Keys.DELETE)
                WebDriverWait(driver, 50).until(lambda driver: driver.find_element(kind, search)).send_keys(inp)
                print(successfully)
                break
            except:
                print(error_message)
                sleep(1)
                continue
            
    def click_a(driver,kind,search,successfully,error_message):
            while True:
                try:
                    bc = driver.find_element(by=kind, value=search)
                    bc.click()
                    print(successfully)
                    break
                except:
                    print(error_message)
                    sleep(1)
                    continue
    

# from Omar_Style_sel import BrowsersProxy as Br

# pr = BrowsersProxy()
# # driver = pr.proxy_firefox("74.249.8.183:3128", "http://whatismyipaddress.com")

# driver = pr.proxy_chrome("103.168.44.41:9191","https://youtu.be/hCtg283iJKg",False)
# sleep(1000)

# dd = Browsers.chrome_b ("https://youtu.be/Qq5bVHRQ7zQ")
# dd.get("https://accounts.google.com/InteractiveLogin/identifier?continue=https%3A%2F%2Fwww.google.com%2F%3Fhl%3Den-US&ec=GAZAmgQ&hl=en&passive=true&ifkv=Af_xneFkB3tG1PGehWiTNPJ0nlCIMbZbRppbIXYIEkdJU-FhTAbL__UJYdBZQn7UOhNhtNJL-lei&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

   
# dd = Browsers.chrome_b("https://youtu.be/Qq5bVHRQ7zQ")
# # print(dd)
# # Browsers.input_a(dd,By.XPATH,'//*[@id="APjFqb"]',"python","SSSS","Eeee")
# Browsers.click_a(dd, By.XPATH, '//*[@id="segmented-like-button"]/ytd-toggle-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]', "SSS", "EEEE")

# # Browsers.click_a(dd,By.XPATH,'//*[@id="segmented-like-button"]/ytd-toggle-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]',"SSS","EEEE")
# # pr = BrowsersProxy()
# # # pr.proxy_firefox("74.249.8.183:3128", "http://whatismyipaddress.com")
# # driver = pr.proxy_chrome("95.56.254.139:3128","http://whatismyipaddress.com", driver_path='E:\\chroo\\chromedriver.exe')










