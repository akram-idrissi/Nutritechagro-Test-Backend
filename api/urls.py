from django.urls import path
from .views import SignUpAPIView, SignInAPIView, ProductDetailAPIView, ProductsByCategoryAPIView

urlpatterns = [
    path('signup/', SignUpAPIView.as_view(), name='signup'),
    path('signin/', SignInAPIView.as_view(), name='signin'),
    path('products/<int:id>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('categories/<str:name>/', ProductsByCategoryAPIView.as_view(), name='products-by-category'),
]
