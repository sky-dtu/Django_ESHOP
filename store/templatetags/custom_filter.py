from django import template

# A decorator "register"
register = template.Library()


# Use decorator to filter and load this in template using "name"
@register.filter(name='currency')
def currency(number):
    raw_text = u"\u20B9"
    # return "₹ " + str(number)
    return raw_text + " " + str(number)


# Use decorator to filter and load this in template using "name"
@register.filter(name='multiply')
def multiply(quantity, price):
    return quantity * price
