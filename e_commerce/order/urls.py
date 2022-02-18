from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('order', views.OrderViewSet)
router.register('orderview', views.OrderItemViewSet)
# router.register('cart', views.CartViewSet)
router.register('coupon', views.CouponViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cart/', views.CartView.as_view(), name="cart"),
    path('cart/add/', views.CartAddView.as_view()),
    path('cart/delete/<int:pk>/', views.CartDelView.as_view()),
]
