import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

USERNAME = "usuario"
PASSWORD = "contraseña"


class EntryAccess:
    # iniciar
    def __init__(self, driverpath):
        self.driver = webdriver.Firefox(service=driverpath)
        print(self.driver)

    def login_university(self):
        self.driver.get("https://virtual.autonoma.edu.pe/CampusVirtual/Default.aspx")
        self.espera_prolongada()

        username_input = self \
            .driver.find_element(By.XPATH, '//*[@id="txtUsuario"]')
        username_input.send_keys(USERNAME)
        self.espera_corta()

        password_input = self.driver.find_element(By.XPATH, '//*[@id="txtPassword"]')
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.ENTER)
        self.espera_larga()
        # ingresar a pagina > zoom
        zoom_button = self.driver.find_element(By.XPATH, '//*[@id="btn-List-Sesions-Virt"]')
        zoom_button.click()

    def entry_class_zoom(self):
        self.espera_prolongada()
        list_class = self.driver.find_elements(By.CSS_SELECTOR,
                                               '#alu_tbody_sesiones_virtuales_programadas_hoy tr td span')
        self.entry_class(list_class)

    def entry_class(self, list_class):
        for clases_zoom in list_class:
            clases = clases_zoom.find_element(By.XPATH,
                                              '/html/body/div[1]/div[2]/div/div/div/div[4]/div/div/div[4]/div[1]/div[3]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/table/tbody/tr/td[7]/span')
            clases.click()


    #orientado a una microempresa -> hilos y monitores -> chat voz
    def permission_success(self):

        self.espera_prolongada()
        self.driver.switch_to(self.driver.window_handles[0])
        self.espera_prolongada()

        self.driver.switch_to.active_element.send_keys(Keys.TAB)
        self.driver.switch_to.active_element.send_keys(Keys.TAB)


    def espera_corta(self):
        time.sleep(1)

    def espera_prolongada(self):
        time.sleep(2)

    def espera_larga(self):
        time.sleep(15)


if __name__ == "__main__":
    bot = EntryAccess(Service(GeckoDriverManager().install()))
    bot.login_university()
    bot.entry_class_zoom()
    bot.permission_success()
