{% extends 'mail_templated/base.tpl'%}

{% block subject %}
Account Activation
{% endblock %}

{% block html %}
سلام {{user_name}}
لطفا جهت فعال سازی اکانت روی لینک زیر کلیک کنید
<a href="http://127.0.0.1:8000/account/api/v1/activation/confirm/{{token}}">active your account</a>
{% endblock %}