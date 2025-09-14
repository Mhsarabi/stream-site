# app/templatetags/jalali.py
from django import template
import jdatetime

register = template.Library()

@register.filter
def jalali(value, fmt="%Y/%m/%d - %H:%M"):
    if not value:
        return ""
    return jdatetime.datetime.fromgregorian(datetime=value).strftime(fmt)