from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from store.models.customer import Customer


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)  # Fetching 'customer' object from database
        error_message = None
        if customer:
            flag = check_password(password, customer.password)  # Checking hashed password
            if flag:
                request.session['customer_id'] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    request.session['email'] = customer.email
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = "Email or Password invalid !!"
        else:
            error_message = "Email or Password invalid !!"

        print(customer)  # Print fetched customer object
        print(email, password)  # Print email, password in terminal window

        return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('login')
