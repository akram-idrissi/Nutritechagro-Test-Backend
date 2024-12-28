from django.urls import path
from .views import SignUpAPIView, SignInAPIView, ProductDetailAPIView, ProductsByCategoryAPIView, ResetPasswordAPIView, CheckoutAPIView, AddOrderAPIView, UserOrdersAPIView

urlpatterns = [
    path('signup/', SignUpAPIView.as_view(), name='signup'),
    path('signin/', SignInAPIView.as_view(), name='signin'),
    path('products/<int:id>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('categories/<str:name>/', ProductsByCategoryAPIView.as_view(), name='products-by-category'),
    path('reset-password/', ResetPasswordAPIView.as_view(), name='reset-password'),
    path('checkout/', CheckoutAPIView.as_view(), name='checkout'),
    path('orders/add/', AddOrderAPIView.as_view(), name='add-order'),
    path('orders/user/<int:id>/', UserOrdersAPIView.as_view(), name='user-orders'),
]
