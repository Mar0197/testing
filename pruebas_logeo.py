from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
service = Service(executable_path='C:\\Users\\Usuario\\Desktop\\MAR\\KINITECH\\app_kinitech\\pruebas_automatizada\\Google_Chrome_166.exe')
# Crea una instancia del controlador de Chrome con las opciones configuradas
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions') 
driver = webdriver.Chrome(executable_path='C:\\Users\\Usuario\\Desktop\\MAR\\KINITECH\\app_kinitech\\pruebas_automatizada\\chromedriver.exe' , options=chrome_options)
# Abre una página web
driver.get('https://feature-dasboard-and-cuentas-cobrar-table.d1b86q7hbj8lbo.amplifyapp.com/auth/login')

# Realiza acciones de prueba aquí (por ejemplo, buscar elementos, hacer clic, etc.)


# Cierra el navegador al final de la prueba
time.sleep(5)
driver.quit()
