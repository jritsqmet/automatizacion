from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


import secrets as st

from time import sleep

driver = webdriver.Chrome()
driver.get("https://campusvirtual.itsqmet.edu.ec/campusV")
sleep(1.5)

botonIngresar = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/div[2]/a")
botonIngresar.click()
sleep(4)

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



##SELECCIONAR REPORTE FINAL
sleep(15)
reporte = driver.find_element(By.XPATH, '//*[@id="__tab_ContentPlaceHolder1_TabContainer1_tabInfFinAsig"]')
reporte.click()
sleep(1000)