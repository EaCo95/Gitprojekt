from behave import *
from CalculateSalary.GherkinTask import *

@given ("5, 4, operator")
def step_impl(context):
    context.tal1 = 5
    context.tal2 = 4
    

@when ("operator is +")
def step_impl(context):
    context.operator = "+"
    context.result = calculator(context.tal1, context.tal2, context.operator)

@then ("return 9")
def step_impl(context):
    assert(context.result == 9)


@given ("7, 4, operator")
def step_impl(context):
    context.tal1 = 7
    context.tal2 = 4
    
@when ("operator is -")
def step_impl(context):
    context.operator = "-"
    context.result = calculator(context.tal1, context.tal2, context.operator)

@then ("return 3")
def step_impl(context):
    assert(context.result == 3)

@given ("6, 3, operator")
def step_impl(context):
    context.tal1 = 6
    context.tal2 = 3

@when ("operator is /")
def step_impl(context):
    context.operator = "/"
    context.result = calculator(context.tal1, context.tal2, context.operator)

@then ("return 2")
def step_impl(context):
    assert(context.result == 2)

@given ("100, 50, operator")
def step_impl(context):
    context.tal1 = 100
    context.tal2 = 50

@when ("operator is *")
def step_impl(context):
    context.operator = "*"
    context.result = calculator(context.tal1, context.tal2, context.operator)

@then ("return 5000")
def step_impl(context):
    assert(context.result == 5000)

@given ("10, 3, operator")
def step_impl(context):
    context.tal1 = 10
    context.tal2 = 3

@when ("operator is %")
def step_impl(context):
    context.operator = "%"
    context.result = calculator(context.tal1, context.tal2, context.operator)

@then ("return 1")
def step_impl(context):
    assert(context.result == 1)
    
