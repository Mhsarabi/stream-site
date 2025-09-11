{% extends 'mail_templated/base.tpl'%}

{% block subject %}
reset password
{% endblock %}

{% block html %}
سلام {{user_name}} برای ریست کردن پسوردت لطفا روی لینک کلیک کن
<a href="http://127.0.0.1:8000/account/reset-password/{{token}}">reset your password</a>
{% endblock %}