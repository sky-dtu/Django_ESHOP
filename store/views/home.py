from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View


# Create your views here.
class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')

        # fetching cart from session
        cart = request.session.get('cart')

        # if cart is present in session
        if cart:
            # create quantity variable after fetching product from cart dictionary
            quantity = cart.get(product)

            # if quantity is available (quantity > 0)
            if quantity:

                # if there is any remove variable, reduce quantity by "1"
                if remove:

                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1

                # if there is no remove variable, add quantity by "1"
                else:
                    cart[product] = quantity + 1

            # if quantity is zero, initialize product quantity = 0
            else:
                cart[product] = 1

        # if cart is "not present" in session
        else:
            # create new cart dictionary and initialize the with product = 1
            cart = {}
            cart[product] = 1
        # Sending the "cart" to session
        request.session['cart'] = cart
        print('CART', request.session['cart'])

        # redirects to "homepage" after clicking "Add to Cart"
        return redirect('homepage')

    def get(self, request):
        cart = request.session.get('')

        if not cart:
            request.session.cart = {}

        products = None

        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')

        if categoryID:
            products = Product.get_all_products_by_category_id(categoryID)
        else:
            products = Product.get_all_products()

        data = {'products': products, 'categories': categories}

        # return HttpResponse('<h1>Index Page</h1>')
        # return render(request, "orders/order.html")
        print('You are ', request.session.get('email'))
        return render(request, "index.html", data)
