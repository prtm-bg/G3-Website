from django.contrib import admin

from .models import material, notice


# Set the admin site header and register models for the admin interface.
admin.site.site_header = 'Group 3 Administration'
admin.site.register(material)
admin.site.register(notice)