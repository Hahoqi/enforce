from django.urls import path

from .views import CheckOutView

app_name = 'orders'

urlpatterns = [
    path('checkout/', CheckOutView.as_view(), name='checkout'),
]
