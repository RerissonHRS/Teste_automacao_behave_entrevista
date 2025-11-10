from behave import given, when, then
import requests

@given("que tenho o endpoint de usuários")
def step_impl(context):
    context.url = "https://jsonplaceholder.typicode.com/users"

@when("eu faço uma requisição pelo ID 1")
def step_impl(context):
    context.response = requests.get(f"{context.url}/1")

@then('o retorno deve conter o nome "Leanne Graham"')
def step_impl(context):
    dados = context.response.json()
    assert dados["name"] == "Leanne Graham"
