from django.contrib import admin
from .models import AttestModel
# Register your models here.
class AdminPanel(admin.ModelAdmin):
    list_display = ['ism', 'tell', 'ruyxatdanUtishVaqti'] 
    

admin.site.register(AttestModel, AdminPanel)