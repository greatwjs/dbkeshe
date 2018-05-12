from django.contrib import admin
from .models import playinfo,classinfo,User

# Register your models here.
class Useradmin(admin.ModelAdmin):
    list_display=('name','password')
class PlayifAdmin(admin.ModelAdmin):
    list_display=('playno','playname','class1','xiangmu','mingci')

class Playadmin(admin.ModelAdmin):
    list_display=('class1','score')

admin.site.register(playinfo,PlayifAdmin)
admin.site.register(classinfo,Playadmin)
admin.site.register(User,Useradmin)