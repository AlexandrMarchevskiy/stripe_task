import stripe
from django.conf import settings
from django.http import JsonResponse
# from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views import View
from .models import Item, Price

stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        price = Price.objects.get(id=self.kwargs["pk"])
        YOUR_DOMAIN = "http://127.0.0.1:8000"  # change in production
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        # return redirect(checkout_session.url)
        return JsonResponse({
            'id': checkout_session.id
        })


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"

class ItemLandingPageView(TemplateView):
    template_name = "landing.html"

    def get_context_data(self, **kwargs):
        item = Item.objects.get(name='Test Product')
        prices = Price.objects.filter(item=item)
        context = super(ItemLandingPageView,
                        self).get_context_data(**kwargs)
        context.update({
            "product": item,
            "prices": prices,
        })
        return context

class ItemPageView(TemplateView):
    template_name = "item.html"

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        product = Item.objects.get(pk=pk)
        context = super(ItemPageView, self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context