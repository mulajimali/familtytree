from django.contrib import admin
from familytree.models import *
# Register your models here.

admin.site.register(MyUser)
admin.site.register(Parents)
admin.site.register(Sibling)
admin.site.register(Children)
admin.site.register(Comment)
