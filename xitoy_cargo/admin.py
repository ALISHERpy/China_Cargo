from django.contrib import admin
from .models import *

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id','fullname',]

admin.site.register(Key)
admin.site.register(Trek)
admin.site.register(Chine_Db)
admin.site.register(Uzbek_Db)
admin.site.register(Available_party)