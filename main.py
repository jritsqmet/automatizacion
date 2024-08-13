from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


import secrets as st

from time import sleep
import os

##############################################################################
def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def set_download_folder(driver, folder_path):
    # Cambia las preferencias de descarga para que se guarde en una carpeta específica
    driver.execute_cdp_cmd('Page.setDownloadBehavior', {
        'behavior': 'allow',
        'downloadPath': folder_path
    })
########################################################################################

driver = webdriver.Chrome()

#driver.maximize_window()  #MAXIMIsA PANTALLA
driver.get("https://campusvirtual.itsqmet.edu.ec/campusV")
sleep(1.5)

botonIngresar = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/div[2]/a")
botonIngresar.click()
sleep(3)

#Ingreso de credenciales
email = driver.find_element(By.XPATH, '//*[@id="i0116"]')
email.send_keys(st.usuario)
email.send_keys(Keys.ENTER)
sleep(2)

password = driver.find_element(By.XPATH, '//*[@id="i0118"]')
password.send_keys(st.contrasenia)
password.send_keys(Keys.ENTER)
sleep(2)


mSesion = driver.find_element(By.XPATH, '//*[@id="idBtn_Back"]')
mSesion.click()
sleep(5)

#ingresar SISACAD
sisa= driver.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div[2]/div[1]/div[1]/form/button/a/h2')
sisa.click()



sleep(2)
driver.switch_to.window(driver.window_handles[1])
driver.get("https://sisacad.itsqmet.edu.ec/ITSQMETIngresoCalificaciones.aspx")


## SELECCIONAR CICLO
select_element= driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_ddlPeriodo"]')
select = Select(select_element)

# Selecciona una opción por valor (atributo 'value')
#select.select_by_value('OCTUBRE 202')

select.select_by_index(9)
sleep(12)
select_elementM = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_ddlAulasVirtuales"]')
selectM = Select(select_elementM)

opciones = selectM.options

for indice in range(len(opciones)):
    print(indice)
    selectM.select_by_index(indice)
    sleep(45)

    ##SELECCIONAR ÁREA REPORTE FINAL
    reporte = driver.find_element(By.XPATH, '//*[@id="__tab_ContentPlaceHolder1_TabContainer1_tabInfFinAsig"]/span')
    reporte.click()
    sleep(1)


    # Descargar
    descargar = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_TabContainer1_tabInfFinAsig_gdInfFinAsig_btnImprimirReporteFinAsig_0"]')
    descargar.click()
    sleep(15)

    ########################################

sleep(1000)






