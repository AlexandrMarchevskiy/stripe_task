from django.contrib import admin
from django.urls import path
from app.views import (
CreateCheckoutSessionView,
SuccessView,
CancelView,
ItemLandingPageView,
ItemPageView
)

urlpatterns = [
    path('', ItemLandingPageView.as_view(), name='landing'),
    path('admin/', admin.site.urls),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('item/<int:pk>', ItemPageView.as_view(), name='item'),
    path('buy/<int:pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')
]
