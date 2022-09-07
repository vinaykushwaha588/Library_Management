from django.contrib import admin
from .models import User,Book
from django.utils.html import format_html
from twilio.rest import Client
from django.conf import settings
# Register your models here.
import math, random

admin.site.site_header='Welcome To Login Vinay'
admin.site.site_title='Welcome to Vinay Dashboard'
admin.site.index_title ='Welcome to Vinay Portal'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email','color_name','mobile','status','is_staff','is_active','is_superuser','is_phone_verified','click_me']
    fields=['email','name','mobile','password','status','is_staff','is_active','is_superuser','is_phone_verified','otp']
    # list_filter= ['mobile']

    # list_display_links = ['color_name'] ##> This line Change Hyperlink
    def get_queryset(self, request):
        qs = User.objects.filter(is_superuser=False)
        print(qs,'<----------user')
        return qs

        

    ## shoerting functions 
    # def less_containt(self,obj):
    #     return obj.email[:15]

    def color_name(self,obj):
        return format_html(f'<span style="color:purple"><b>{ obj.name }</b></span>')

    def click_me(self,obj):
        return format_html(f'<button style="color:green"><a href="/admin/account/user/{obj.id}/change/">view</a></button></span>')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['book_name','book_title','book_author']