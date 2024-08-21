
from rest_framework import serializers

from . models import Product

from django.contrib.auth.models import User



class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = ['id', 'name', 'description', 'price']
        


class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True, required=True)


    class Meta:

        model = User
        fields = ['username', 'email', 'password', 'password2']

        extra_kwargs = {

            'password': {'write_only': True}

        }


    def save(self):

        user = User(

            username=self.validated_data['username'],
            email=self.validated_data['email'],

        )

        password=self.validated_data['password']
        password2=self.validated_data['password2']

 
        if password != password2:

            raise serializers.ValidationError({'password': 'Sorry, the passwords did not match'})


        user.set_password(password)
        user.save()

        return user



