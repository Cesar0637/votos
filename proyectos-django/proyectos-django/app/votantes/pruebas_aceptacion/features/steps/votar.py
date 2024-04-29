from behave import when, given, then
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

@given(u'que ingreso a la url "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)


@given(u'presiono el boton votar')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/form/table/tbody/tr[1]/td[6]/a").click()


@when(u'voy para los resultados')
def step_impl(context):
    time.sleep(2)
    context.driver.get("http://localhost:8000/listaCandidatosP/")
    time.sleep(3)


@then(u'Entonces puedo ver el un voto mas para cesar')
def step_impl(context):
    time.sleep(5)
    