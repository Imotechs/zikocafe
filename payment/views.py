from django.shortcuts import render,redirect
from django.template import Context
from django.views import View
from django.views.generic import TemplateView
import stripe
from django.conf import settings
from django.http import JsonResponse
from payment.models import Product
from django.views.decorators.csrf import csrf_exempt


stripe.api_key = settings.STRIPE_SECRET_KEY

class CreatCheckoutSessionView(View):
    def post(self,request,*args, **kwargs):
        # product_id = self.kwargs["pk"]
        # product_price = request.POST['product_price']
        
        # product = Product.objects.get(id=product_id)
        # stripe.Product.create(name=product.name)
        #print(product_price)
        product_id = self.kwargs["pk"]
        product = Product.objects.get(id=product_id)
        YOUR_DOMAIN = 'http://127.0.0.1:8000'

        try:
            checkout_session = stripe.checkout.Session.create(
            payment_method_types = ['card'],
           line_items=[
               {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                'price_data': {
                    'unit_amount': product.price,
                    'currency': 'usd',
                    'product_data': {
                        'name':product.name,
                    },
                    },
                    'quantity': 1,
                    },
        
            ],
        mode='payment',
        success_url=YOUR_DOMAIN + '/success/',
        cancel_url=YOUR_DOMAIN + '/failure/',
        )
        except Exception as e:
            return str(e)

        return redirect(checkout_session.url, code=303)




class ProductLandingView(TemplateView):
    product =Product.objects.all()
    template_name = 'payment/landing.html'
    def get_context_data(self, **kwargs: any):
        product =Product.objects.all()
        context = super(ProductLandingView,self).get_context_data(**kwargs)
        context.update({
            'product':product,
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
        })
        return context

class PaymentSucces(TemplateView):
    template_name = 'payment/success.html'

class PaymentFails(TemplateView):
    template_name = 'payment/Failure.html'