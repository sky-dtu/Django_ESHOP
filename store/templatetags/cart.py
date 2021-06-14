from django import template

# A decorator "register"
register = template.Library()


# Use decorator to filter and load this in template using "name"
@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    # Return already available products in cart
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True

    return False


@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    # Return already available products in cart
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    # print(product, cart)
    return 0


@register.filter(name='price_total')
def price_total(product, cart):
    # Return product price * quantity
    return product.price * cart_quantity(product, cart)


@register.filter(name='total_cart_price')
def total_cart_price(product, cart):
    sum = 0
    for p in product:
        sum += price_total(p, cart)
    return sum
