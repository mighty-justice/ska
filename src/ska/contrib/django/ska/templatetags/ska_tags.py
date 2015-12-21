from django import template
from django.conf import settings
from django.core.urlresolvers import reverse

from ska import sign_url

register = template.Library()

TWENTY_FOUR_HOURS_IN_SECONDS = 24*60*60

@register.simple_tag
def signed_url(user, lifetime=TWENTY_FOUR_HOURS_IN_SECONDS):
    return sign_url(auth_user=user.username, secret_key=settings.SKA_SECRET_KEY, url=reverse('ska.login'), lifetime=lifetime)