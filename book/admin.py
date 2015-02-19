from django.contrib import admin

# Register your models here.
#from book.models import User
#admin.site.register(User)


from django.contrib.auth.models import User

from django.contrib.auth.admin import UserAdmin 
from book.models import UserProfile,Catagory,Product,Cart

class CatagoryAdmin(admin.ModelAdmin):
	list_display = ('cname','purdate','createdby')

class ProductAdmin(admin.ModelAdmin):
	list_display = ('pname','cid','price','noitem')

class CartAdmin(admin.ModelAdmin):
	list_display = ('uid','pid','noitem','purdate','deldate','status')
 
class UserProfileInline(admin.StackedInline):
    """ As you are noticed your profile will be edited as inline form """
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'userprofile'
 
class UserAdmin(UserAdmin):
    """ Just add inlines to the original UserAdmin class """
    # list_display = ('user','address','phone')
    inlines = [UserProfileInline, ]
 

    admin.site.unregister(User)

    admin.site.register(UserProfile)
    admin.site.register(Catagory, CatagoryAdmin)
    admin.site.register(Product, ProductAdmin)
    admin.site.register(Cart, CartAdmin)
    admin.site.register(User, UserAdmin)