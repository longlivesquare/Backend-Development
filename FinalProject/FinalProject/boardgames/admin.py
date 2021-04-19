from django.contrib import admin
from .models import Boardgame,Category

# Register your models here.

admin.site.register(Boardgame)
admin.site.register(Category)