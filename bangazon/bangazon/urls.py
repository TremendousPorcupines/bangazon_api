"""bangazon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken import views
from bangazon_api.views import line_item_view, customer_view, order_view, payment_view, product_type_view, product_view

router = routers.DefaultRouter()
router.register(r'products', product_view.ProductViewSet)
router.register(r'product_types', product_type_view.ProductTypeViewSet)
router.register(r'line_items', line_item_view.LineItemViewSet)
router.register(r'orders', order_view.OrderViewSet)
router.register(r'customers', customer_view.CustomerViewSet)
router.register(r'payment_types', payment_view.PaymentTypeViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^is_auth/', customer_view.IsAuth.as_view()),
]
