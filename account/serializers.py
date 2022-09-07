
from asyncio.windows_events import NULL
from rest_framework import serializers
from .models import User,Book
import random


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['email','password','name','mobile', 'otp']
        

    def validate(self, attrs):
        mobile = attrs.get('mobile')
        name = attrs.get('name')
        otp = attrs.get('otp')
        if str(mobile).isdigit() and len(mobile)==10:
            if str(name).isalpha():
                    return attrs
            else:
                raise serializers.ValidationError("Enter a valid name")
        else:
            raise serializers.ValidationError("Enter a valid mobile number ")
        
    # def create(self, validated_data):
    #     user = super(UserSerializer, self).create(validated_data)
    #     user.set_password(validated_data['password'])

    #     def random_with_N_digits(n):
    #         range_start = 10**(n-1)
    #         range_end = (10**n)-1
    #         return random.randint(range_start, range_end)

    #     otp = random_with_N_digits(6)
    #     user.otp = otp
    #     user.save()

    #     subject = 'Please Confirm Your Account'
    #     message = 'Your 6 Digit Verification Pin: {}'.format(otp)
    #     email_from = '*****'
    #     recipient_list = [str(user.email), ]
    #     send_mail(subject, message, email_from, recipient_list)
    #     return user


    

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50)
    class Meta:
        model = User
        fields = ["email", "password"]
    
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"