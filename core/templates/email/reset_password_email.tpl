{% extends 'mail_templated/base.tpl' %}

{% block subject %}
بازیابی رمز عبور
{% endblock %}

{% block html %}
<div style="direction: rtl; text-align: right; font-family: Tahoma, Arial, sans-serif; font-size: 14px; line-height: 1.8; color: #333;">
    <p>سلام {{ user_name }} عزیز،</p>
    <p>برای بازیابی رمز عبور خود لطفاً روی دکمه زیر کلیک کنید:</p>
    <p>
        <a href="http://127.0.0.1:8000/account/reset-password/{{ token }}" 
           style="display: inline-block; background-color: #2196F3; color: #fff; padding: 10px 20px; text-decoration: none; border-radius: 5px;">
           بازیابی رمز عبور
        </a>
    </p>
    <p>اگر شما این درخواست را ارسال نکرده‌اید، این پیام را نادیده بگیرید.</p>
</div>
{% endblock %}