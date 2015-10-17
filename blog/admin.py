from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Vprasanje, Odgovor


class OdgovorInline(admin.TabularInline):
    model = Odgovor
    fk_name = "vprasanje"

class VprasanjeAdmin(admin.ModelAdmin):

    inlines = [
        OdgovorInline,
    ]


admin.site.register(Vprasanje, VprasanjeAdmin)