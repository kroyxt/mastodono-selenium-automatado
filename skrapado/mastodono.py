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
import wget


load_dotenv()


class Mastodon(webdriver.Firefox):
    def __init__(self):
        self.service = FirefoxService(GeckoDriverManager().install())
        # self.options = Options()
        # self.options.add_argument("-headless")
        # super(Mastodon, self).__init__(options=self.options)
        super(Mastodon, self).__init__()
        self.wait = WebDriverWait(self, 60)
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

    def elsxutu_bildojn(self, vorto):
        sercxilo = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='compose-panel']/div[@class='search']/input")
            )
        )
        sercxilo.clear()
        sercxilo.send_keys(f"{vorto} has:image")
        sercxilo.send_keys(Keys.ENTER)

        afisxa_modo = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='account__section-headline']/button[child::span[contains(text(), 'Afiŝoj')]]")
            )
        )
        afisxa_modo.click()
        afisxa_modo.send_keys(Keys.PAGE_DOWN)
        afisxa_modo.send_keys(Keys.PAGE_DOWN)

        bildoj = self.wait.until(
            EC.visibility_of_all_elements_located(
                (By.XPATH, "//a[@class='media-gallery__item-thumbnail']/img")
            )
        )

        bildaj_ligiloj = [bildo.get_attribute('src') for bildo in bildoj]

        vojo = os.getcwd()
        kunigita_vojo = os.path.join(vojo, "bildoj")
        if not os.path.exists(kunigita_vojo):
            os.mkdir(kunigita_vojo)

        for ligilo in bildaj_ligiloj:
            savu_kiel = os.path.join(kunigita_vojo, os.path.basename(ligilo))
            wget.download(ligilo, savu_kiel)
            print(f"Dosiero '{os.path.basename(ligilo)} savatas en {savu_kiel}'")

    def malsxaltu(self):
        self.quit()
