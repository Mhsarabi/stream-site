from .serializers import RegistrationSerializer,CustomTokenObtainPairSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics,status
from rest_framework.response import Response
from mail_templated import EmailMessage
from user_profile.api.utils import EmailThreading
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from user_profile.models import User
from django.conf import settings
from django.http import HttpResponseRedirect
from jwt.exceptions import ExpiredSignatureError,InvalidSignatureError
import jwt

# register
class RegistrationApiView(generics.GenericAPIView):
    serializer_class=RegistrationSerializer
    
    def post(self,request,*args,**kwargs):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user_name = serializer.validated_data['user_name']
            email=serializer.validated_data['email']
            

            user_obj=get_object_or_404(User,email=email)
            token=self.get_token_for_user(user_obj)
            email_obj=EmailMessage('email/activation_email.tpl',{'token':token,'user_name': user_name},'admin@admin.com',to=[email])
            EmailThreading(email_obj).start()
            data={
                'user_name': user_name,
                'email': email,
            }
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get_token_for_user(self,user):
        refresh=RefreshToken.for_user(user)
        return str(refresh.access_token)

# login  
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class=CustomTokenObtainPairSerializer

class ActivationApiView(APIView):
    def get(self,request,token,*args,**kwargs):
        try:
            token=jwt.decode(token,settings.SECRET_KEY,algorithms=['HS256'])
            user_id=token.get("user_id")
        except ExpiredSignatureError:
            return Response({'details':'token has been expired'},status=status.HTTP_400_BAD_REQUEST)
        except InvalidSignatureError:
            return Response({'details':'token is not valid'},status=status.HTTP_400_BAD_REQUEST)
        
        user_obj=User.objects.get(pk=user_id)
        if user_obj.is_verified:
            return Response({'details':'your account has already verified'},status=status.HTTP_400_BAD_REQUEST)
        user_obj.is_verified=True
        user_obj.save()
        return HttpResponseRedirect('/account/login')