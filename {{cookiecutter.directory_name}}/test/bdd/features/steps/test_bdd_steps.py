from behave import *
from expycted import expect

from {{cookiecutter.project_name}} import hello

@given('a name "Jozo"')
def _(context):
    context.name = 'Jozo'

@when('we call a function hello with said name')
def _(context):
    context.result = hello(context.name)

@then('it will return "Hello, Jozo"')
def _(context):
    expect(context.result).to.be_equal_to("Hello, Jozo")