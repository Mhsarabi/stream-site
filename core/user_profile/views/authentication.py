from django.views.generic import FormView,DetailView
from django.shortcuts import redirect, get_object_or_404
from django.core.mail import EmailMessage
from django.conf import settings
from django.urls import reverse_lazy
import jwt
from user_profile.forms import RegisterUserForm,LoginForm
from user_profile.models import User
from user_profile.email_connection.utils import EmailThreading  
from django.http import HttpResponseRedirect
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError
from django.views import View
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render

# Create your views here.
class RegistrationView(FormView):
    template_name = "account/sign_up.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy("profile:login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password1"])
        user.is_active = True
        user.is_verified = False
        user.save()


        token = jwt.encode({"user_id": user.id}, settings.SECRET_KEY, algorithm="HS256")

        message = render_to_string(
            'email/activation_email.tpl',
            {'token': token, 'user_name': user.user_name}
        )
        email_obj = EmailMessage(
            "فعال‌سازی حساب کاربری",
            message,
            "admin@admin.com",
            to=[user.email],
        )
        email_obj.content_subtype = "html"
        EmailThreading(email_obj).start()

        return super().form_valid(form)

class ActivationView(View):
    def get(self, request, token, *args, **kwargs):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = payload.get("user_id")
        except ExpiredSignatureError:
            return redirect("/account/login/?error=expired")
        except InvalidSignatureError:
            return redirect("/account/login/?error=invalid")

        user = get_object_or_404(User, pk=user_id)
        if not user.is_verified:
            user.is_verified = True
            user.save()

        return HttpResponseRedirect("/account/login/")
    
class login_user(FormView):
    template_name = 'account/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('movie:main')  
    def form_valid(self, form):
        user = form.cleaned_data['user']
        login(self.request, user)  
        messages.success(self.request, f"به سایت خوش آمدید {user.user_name}!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "نام کاربری یا رمز عبور اشتباه است.")
        return super().form_invalid(form)



class PasswordResetRequestView(View):
    template_name = "account/reset_password.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get("email")
        user = User.objects.filter(email=email).first()
        if not user:
            return render(request, self.template_name, {"error": "کاربری با این ایمیل یافت نشد."})

        token = jwt.encode({"user_id": user.id}, settings.SECRET_KEY, algorithm="HS256")
        
        message = render_to_string(
            'email/reset_password_email.tpl',
            {'token': token, 'user_name': user.user_name}
        )
        email_obj = EmailMessage(
            "بازیابی رمز عبور",
            message,
            "admin@admin.com",
            to=[user.email],
        )
        email_obj.content_subtype = "html"
        EmailThreading(email_obj).start()

        return render(request, "account/reset_password_email_sent.html", {"email": email})


class PasswordResetConfirmView(View):
    template_name = "account/password_reset_confirm.html"

    def get(self, request, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = payload["user_id"]
            request.session["reset_user_id"] = user_id
            return render(request, self.template_name)
        except jwt.ExpiredSignatureError:
            return render(request, "account/password_reset_invalid.html", {"error": "لینک منقضی شده است."})
        except jwt.InvalidTokenError:
            return render(request, "account/password_reset_invalid.html", {"error": "توکن معتبر نیست."})

    def post(self, request, token):
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2:
            return render(request, self.template_name, {"error": "رمز عبور و تکرارش یکسان نیستند."})

        user_id = request.session.get("reset_user_id")
        user = get_object_or_404(User, id=user_id)
        user.set_password(password1)
        user.save()

        return render(request, "account/password_reset_done.html")