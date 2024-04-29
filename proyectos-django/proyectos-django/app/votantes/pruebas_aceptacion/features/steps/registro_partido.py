from behave import when, given, then
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

@given(u'presiono el boton Nuevo partido')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/a[1]").click()


@given(u'escribo el nombre del partido "{partidoname}" y su descripcion "{desc}"')
def step_impl(context,partidoname,desc):
    time.sleep(5)
    context.driver.find_element(By.ID, "id_nombre").send_keys(partidoname)
    context.driver.find_element(By.ID, "id_descripcion").send_keys(desc)
    time.sleep(5)


@when(u'presiono el boton Guardar')
def step_impl(context):
    time.sleep(10)
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/form/input[2]").click()
    time.sleep(5)


@then(u'Entonces puedo ver el candidato margarito en la lista de candidatos.')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element(By.XPATH, '/html/body/div[1]/nav/ul[1]/li[2]/a')