from django.contrib import admin
from .models import Auto

# Register your models here.
class AutoAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')

admin.site.register(Auto, AutoAdmin)
