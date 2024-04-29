from behave import when, given, then
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver


@given(u'presiono el boton de Nuevo candidato')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/a").click()


@given(u'escribo el nombre "{name}" y su apeido paterno "{ap}" y su apeido materno "{am}"')
def step_impl(context,name,ap,am):
    time.sleep(5)
    context.driver.find_element(By.ID, "id_nombre").send_keys("margarito")
    context.driver.find_element(By.ID, "id_apeido_Paterno").send_keys("ruiz")
    context.driver.find_element(By.ID, "id_apeido_Materno").send_keys("salas")
    time.sleep(5)


@given(u'selecciono su partido "{partido}"')
def step_impl(context,partido):
    time.sleep(5)
    x = context.driver.find_element(By.ID, "id_partidos")

    drop=Select(x)


    drop.select_by_visible_text("naranja")
    time.sleep(5)
@when(u'presiono el boton de Guardar')
def step_impl(context):
    time.sleep(10)
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/form/input[2]").click()
    time.sleep(5)


@then(u'puedo ver el candidato margarito en la lista de candidatos.')
def step_impl(context):
    time.sleep(5)
    context.driver.get("http://localhost:8000/listaC/")