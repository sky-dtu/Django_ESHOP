from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views import View
from store.models.customer import Customer


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST

        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        print(first_name, last_name, phone, email, password)

        # validation
        value = {'first_name': first_name,
                 'last_name': last_name,
                 'phone': phone,
                 'email': email,
                 }

        # creating object
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        error_message = self.validateCustomer(customer)

        # saving
        if not error_message:
            # hashing password
            customer.password = make_password(customer.password)

            # register object
            customer.register()

            # redirects to homepage after signup success
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

        # return HttpResponse(request.POST.get('email'))
        # return HttpResponse("Signup Success")

    def validateCustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 3:
            error_message = "First Name must be minimum 3 characters long"
        elif not customer.last_name:
            error_message = "Last Name Required !!"
        elif len(customer.last_name) < 3:
            error_message = "Last Name must be minimum 3 characters long"
        elif not customer.phone:
            error_message = "Phone Number Required !!"
        elif len(customer.phone) < 10:
            error_message = "Phone Number must be minimum 10 characters long"
        elif not customer.email:
            error_message = "Email ID Required !!"
        elif not customer.password:
            error_message = "Password Required !!"
        elif len(customer.password) < 8:
            error_message = "Password must be minimum 8 characters long"
        elif len(customer.password) > 15:
            error_message = "Password cannot have more than 15 characters"
        # Checking email validation
        elif customer.isExists():
            error_message = 'Email Address already registered.'

        return error_message
