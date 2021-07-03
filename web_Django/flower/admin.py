from django.contrib import admin
from flower.models import Department
# Register your models here.
'''1'''
# admin.site.register(Department)#
'''2'''
@admin.register(Department)
class DepAdmin(admin.ModelAdmin):
    list_display = ('id','departmentname',)
    list_display_links = ('departmentname',)#可进入编辑
    list_per_page = 10#分页
    ordering = ('id',)
    # list_editable = ('departmentname',)#可编辑
