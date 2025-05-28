from django.contrib import admin

# Register your models here.

from .models import Subscribe,Partners,Contact,ContactUs

admin.site.register(Subscribe)
admin.site.register(Partners)
admin.site.register(Contact)
admin.site.register(ContactUs)
