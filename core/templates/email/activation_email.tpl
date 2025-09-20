{% extends 'mail_templated/base.tpl' %}

{% block subject %}
فعال‌سازی حساب کاربری
{% endblock %}

{% block html %}
<div style="direction: rtl; text-align: right; font-family: Tahoma, Arial, sans-serif; font-size: 14px; line-height: 1.8; color: #333;">
    <p>سلام {{ user_name }} عزیز،</p>
    <p>لطفاً جهت فعال‌سازی حساب کاربری خود روی لینک زیر کلیک کنید:</p>
    <p>
        <a href="http://127.0.0.1:8000/account/activation/confirm/{{ token }}/" 
           style="display: inline-block; background-color: #4CAF50; color: #fff; padding: 10px 20px; text-decoration: none; border-radius: 5px;">
           فعال‌سازی حساب
        </a>
    </p>
    <p>اگر شما این درخواست را ارسال نکرده‌اید، این پیام را نادیده بگیرید.</p>
</div>
{% endblock %}