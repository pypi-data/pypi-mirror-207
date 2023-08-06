import os
import logging
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from autotest.lib.configurations.common_config import chromiumUserAgent, chromeUserAgent, chromeDriverPathLinux, geckoDriverPathWin, \
    edgeDriverPathWin, waitTime, environment, chromeDriverPathWin
from webdriver_manager.chrome import ChromeDriverManager

class setup:


    def loadURL(self, browserType, env):
        driver = None

        # Set the threshold for selenium to INFO
        from selenium.webdriver.remote.remote_connection import LOGGER as seleniumLogger
        seleniumLogger.setLevel(logging.INFO)
        # Set the threshold for urllib3 to INFO
        from urllib3.connectionpool import log as urllibLogger
        urllibLogger.setLevel(logging.INFO)

        if (browserType == "headless-chrome"):
            from selenium.webdriver.chrome.options import Options
            print("in headless chrome")
            chrome_options = Options()
            chrome_options.add_argument("user-agent="+chromeUserAgent)
            chrome_options.add_argument('--headless')
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--window-size=1980,1080")
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument('--allow-running-insecure-content')
            chrome_options.add_argument("--allow-insecure-localhost")
            chrome_options.add_argument('--ignore-ssl-errors')
            chrome_options.set_capability("acceptInsecureCerts", True)
            chrome_options.add_argument('--log-level=1')
            driver = webdriver.Chrome(ChromeDriverManager().install())
            #driver = webdriver.Chrome(options=chrome_options, executable_path=chromeDriverPathLinux, service_log_path='NUL')


        elif (browserType == "headless-firefox"):
            from selenium.webdriver.firefox.options import Options
            print("in headless firefox")
            firefox_options = Options()
            firefox_options.headless = True
            driver = webdriver.Firefox(options=firefox_options, executable_path=geckoDriverPathWin, service_log_path=os.devnull)


        elif (browserType == "chrome"):
            from selenium.webdriver.chrome.options import Options
            print("in headed chrome")
            chrome_options = Options()

            chrome_options.add_argument('--log-level=1')
            driver = webdriver.Chrome(options=chrome_options, executable_path=chromeDriverPathLinux, service_log_path='NUL')



        elif (browserType == "firefox"):
            print("in headed firefox")
            driver = webdriver.Firefox(executable_path=geckoDriverPathWin, service_log_path=os.devnull)


        elif (browserType == "edge"):
            print("in headed edge")
            driver = webdriver.Edge(executable_path=edgeDriverPathWin, service_log_path=os.devnull)


        elif (browserType == "headless-chromium"):
            from selenium.webdriver.chrome.options import Options
            print("in headless chromium")
            chrome_options = Options()
            chrome_options.add_argument("user-agent=" + chromeUserAgent)
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-signin-frame-client-certs')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--v=99')
            chrome_options.add_argument('--single-process')
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--window-size=1980x1080")
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument('--allow-running-insecure-content')
            chrome_options.add_argument("--allow-insecure-localhost")
            chrome_options.add_argument('--ignore-ssl-errors')
            chrome_options.set_capability("acceptInsecureCerts", True)
            chrome_options.add_argument('--log-level=1')
            chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
            chrome_options.binary_location = "D:/Installers/Browsers/chromium_win_v86.0.4240.111-r800218/chrome.nosync/Chrome-bin/chrome.exe"
            driver = webdriver.Chrome(executable_path="D:/Installers/Browsers/chromium_win_v86.0.4240.111-r800218/chrome.nosync/Chrome-bin/chromedriver.exe", options=chrome_options, service_log_path='NUL')


        elif (browserType == "chromium-aws"):
            from selenium.webdriver.chrome.options import Options
            print("in headless aws chromium")
            chrome_options = Options()
            # chrome_options.add_argument("user-agent=" + chromiumUserAgent)
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-setuid-sandbox')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--single-process')
            chrome_options.add_argument('--disable-signin-frame-client-certs')
            chrome_options.add_argument("--window-size=1980x1080")

            chrome_options.binary_location = "/tmp/bin/headless-chromium"
            chrome_options.binary_location = "D:/Installers/Browsers/chromium_win_v86.0.4240.111-r800218/chrome.nosync/Chrome-bin/chrome.exe"
            driver = webdriver.Chrome(executable_path="D:/Installers/Browsers/chromium_win_v86.0.4240.111-r800218/chrome.nosync/Chrome-bin/chromedriver.exe", options=chrome_options, service_log_path='NUL')


        elif(browserType == "chrome-aws"):
            from selenium.webdriver.chrome.options import Options
            print("in headless aws chromium")
            chrome_options = Options()
            chrome_options.add_argument("user-agent=" + chromiumUserAgent)
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-setuid-sandbox')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--v=99')
            chrome_options.add_argument('--single-process')
            chrome_options.add_argument('--disable-signin-frame-client-certs')

            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--window-size=1980x1080")
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument('--allow-running-insecure-content')
            chrome_options.add_argument("--allow-insecure-localhost")
            chrome_options.add_argument('--ignore-ssl-errors')
            chrome_options.set_capability("acceptInsecureCerts", True)
            chrome_options.add_argument('--log-level=1')
            chrome_options.add_argument('--homedir=/tmp')
            chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_experimental_option('useAutomationExtension', False)

            # chrome_options.add_argument('--v=99')
            # chrome_options.add_argument("remote-debugging-port=443")
            # chrome_options.add_argument('--ignore-certificate-errors')
            # chrome_options.add_argument('--allow-running-insecure-content')
            # chrome_options.add_argument("--allow-insecure-localhost")
            # chrome_options.add_argument('--ignore-ssl-errors')
            # chrome_options.set_capability("acceptInsecureCerts", True)
            # chrome_options.add_argument('--log-level=1')

            chrome_options.add_argument('--user-data-dir=/tmp/user-data')
            chrome_options.add_argument('--data-path=/tmp/data-path')

            chrome_options.add_argument('--homedir=/tmp')
            chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_experimental_option('useAutomationExtension', False)

            chrome_options.binary_location = "/tmp/bin/headless-chromium"
            driver = webdriver.Chrome(executable_path="/tmp/bin/chromedriver", options=chrome_options,
                                      service_log_path='/tmp/task/results/chromedriver3.log')



        print("User Agent = " + driver.execute_script("return navigator.userAgent"))
        print("Chrome Version = " + driver.capabilities['browserVersion'])
        print("ChromeDriver version = " + driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0])
        print(driver.get_window_size())
        driver.maximize_window()
        print(driver.get_window_size())
        wait = WebDriverWait(driver, waitTime)
        #driver.get(environment[env]["baseURL"])
        return driver, wait

