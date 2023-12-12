from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
import skrapado.konstantoj as konst
from dotenv import load_dotenv
import os


load_dotenv()


class Mastodon(webdriver.Firefox):
    def __init__(self):
        self.service = FirefoxService(GeckoDriverManager().install())
        # self.options = Options()
        # self.options.add_argument("-headless")
        # super(Mastodon, self).__init__(options=self.options)
        super(Mastodon, self).__init__()
        self.wait = WebDriverWait(self, 30)
        self.maximize_window()

    def iru_al_cxefpagxo(self):
        self.get(konst.BAZA_LIGILO)

    def ensalutu(self):
        butono_al_ensaluto = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[@class='button button--block button-tertiary'][@href='/auth/sign_in']")
            )
        ).click()

        retposxto = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@id='user_email']")
            )
        )
        retposxto.clear()
        retposxto.send_keys(os.getenv("RETPOSXTO"))

        pasvorto = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@id='user_password']")
            )
        )
        pasvorto.clear()
        pasvorto.send_keys(os.getenv("PASVORTO"))

        ensaluta_butono = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'Log in')]")
            )
        ).click()
