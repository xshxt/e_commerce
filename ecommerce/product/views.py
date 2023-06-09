from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework import generics , permissions
from django.shortcuts import render
from .models import*
from .serializers import*
from rest_framework.viewsets import ModelViewSet
from product.pagination import APIListPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth import login
from .permissons import IsOwnerOrReadOnly
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


#Login API
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)



#API Products
class ProducteModelViewSet(ModelViewSet):
    queryset = Producte.objects.all()
    serializer_class = ProducteSerializer
    permission_classes = (IsOwnerOrReadOnly, ) 




#API Category
class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )  



#prodcuts in category
class CategotyProductsModelViewSet(ModelViewSet):
    queryset = Producte.objects.all()
    serializer_class = CategotyProducts
    permission_classes = (IsAuthenticatedOrReadOnly, )    



#API Atribute
class AtributeModelViewSet(ModelViewSet):
    queryset = Atribute.objects.all()
    serializer_class = AtributeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, ) 



#API Photo
class PhotoModelViewSet(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


#API Cartitem
class OrderItemModelViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


#API Basket
class OrderModelViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )



# Create your views here.
def all_products(request):
    product= Producte.objects.all()
    categoory = Category.objects.all()
    atribute = Atribute.objects.all()
    
    context={
        'product':product,
        'categoory': categoory,
        'atribute':atribute,
    }
    return render(request,'all_prod.html',context)
