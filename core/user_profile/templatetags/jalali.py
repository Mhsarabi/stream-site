# app/templatetags/jalali.py
from django import template
import jdatetime
import pytz

register = template.Library()

@register.filter
def jalali(value, fmt="%Y/%m/%d - %H:%M"):
    if not value:
        return ""
    tehran_tz = pytz.timezone("Asia/Tehran")
    value = value.astimezone(tehran_tz)
    return jdatetime.datetime.fromgregorian(datetime=value).strftime(fmt)