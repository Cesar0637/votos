import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()

driver.get("http://localhost:8000/listaP/")
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/a[1]").click()

driver.find_element(By.ID, "id_nombre").send_keys("partido verde")
driver.find_element(By.ID, "id_descripcion").send_keys("Verde")
time.sleep(15)
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/form/input[2]").click()

time.sleep(2)

driver.get("http://localhost:8000/listaC/")
time.sleep(2)


driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/a").click()
driver.find_element(By.ID, "id_nombre").send_keys("trump")
driver.find_element(By.ID, "id_apeido_Paterno").send_keys("valVerde")
driver.find_element(By.ID, "id_apeido_Materno").send_keys("gutierrez")
x = driver.find_element(By.ID, "id_partidos")

drop=Select(x)


drop.select_by_visible_text("pan")
time.sleep(15)
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/form/input[2]").click()

driver.get("http://localhost:8000/votaciones/")
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/form/table/tbody/tr[1]/td[6]/a").click()
time.sleep(3)
driver.get("http://localhost:8000/listaCandidatosP/")
time.sleep(5)
