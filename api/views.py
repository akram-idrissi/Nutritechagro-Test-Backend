import uuid

from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer
from .serializers import ProductSerializer, UserSerializer


class SignUpAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SignInAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            serializer = UserSerializer(user)
            return Response({"message": "Sign-in successful.", "user": serializer.data}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

class ProductDetailAPIView(APIView):
    def get(self, request, id):
        try:
            product = Product.objects.get(pk=id)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

class ProductsByCategoryAPIView(APIView):
    def get(self, request, name):
        products = Product.objects.filter(category=name)
        paginator = Paginator(products, 5)  
        page_number = request.query_params.get('page', 1)
        page_obj = paginator.get_page(page_number)
        serializer = ProductSerializer(page_obj.object_list, many=True)
        return Response({
            "products": serializer.data,
            "total_pages": paginator.num_pages,
            "current_page": page_obj.number
        }, status=status.HTTP_200_OK)

class SimilarProductsAPIView(APIView):
    def get(self, request, category_name, product_id):
        similar_products = Product.objects.filter(category=category_name).exclude(id=product_id)[:10]
        serializer = ProductSerializer(similar_products, many=True)
        return Response({
            "products": serializer.data,
            "total_products": len(similar_products),
        }, status=status.HTTP_200_OK)

class ResetPasswordAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email_or_username = request.data.get('email_or_username')
        new_password = request.data.get('new_password')

        if not email_or_username or not new_password:
            return Response(
                {"error": "Both email/username and new password are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = User.objects.get(email=email_or_username) if "@" in email_or_username else User.objects.get(username=email_or_username)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        if len(new_password) < 8:
            return Response(
                {"error": "Password must be at least 8 characters long."},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.set_password(new_password)
        user.save()
        return Response({"message": "Password reset successfully."}, status=status.HTTP_200_OK)

class CheckoutAPIView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]

    def post(self, request):
        return Response({"message": "Checkout successful."}, status=status.HTTP_200_OK)

class AddOrderAPIView(APIView):

    def post(self, request):
        data = request.data
        data['orderID'] = str(uuid.uuid4()) 
        data['status'] = 'success'
        data['user'] = data['id']
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserOrdersAPIView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request, id):
        orders = Order.objects.filter(user=id)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
