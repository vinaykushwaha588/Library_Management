from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserLoginSerializer,BookSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Book, User
from rest_framework import viewsets
from rest_framework import status
from django.contrib.auth.hashers import make_password
from .helpers import send_otp_to_phone
from django.core.exceptions import PermissionDenied

    
class SignUpUser(APIView):
    def post(self,request):
        data = request.data
        email = data.get('email')
        name = data.get('name')
        password = data.get('password')
        if data.get('mobile') is None:
            return Response({
                'status' : 400,
                'message': "Mobile Number is Required"
            })
        if data.get('password') is None:
            return Response({
                'status' : 400,
                'message': "password is Required"
            })
        user = User.objects.create(email=email,name=name,
            mobile = data.get('mobile'),
            otp = send_otp_to_phone(data.get('mobile'))
            )
        user.password = make_password(password)
        user.save()
        return Response({
            'status':200,
            'msg':"Otp hass been send & Account Crated..."
        })

class verifyOTPView(APIView):
    def post(self, request):
        email = request.data["email"]
        otp = int(request.data["otp"])
        user = User.objects.get(email=email)
        if int(user.otp)==otp:
            user.is_phone_verified = True
            user.save()
            return Response("Verification Successfull")
        else:
            raise PermissionDenied("OTP Verification failed")

class LoginUser(APIView):
    def post(self,request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email=email, password=password)
            print(user,"<40-------Authenticated User")
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({"refresh": str(refresh), "access": str(refresh.access_token)})
            else:
                return Response({"error": "Invalid user credientials!"})


class BookList(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 
    queryset = Book.objects.all()
    serializer_class = BookSerializer
        




