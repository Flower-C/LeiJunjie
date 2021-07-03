from django.db import models

# Create your models here.
class Department(models.Model):
    #定义属性：默认主键自增id字段可不写
    id = models.AutoField('编号',primary_key=True)#''
    departmentname = models.CharField('名称',max_length=10)#'名称' 可直接用于前端展示
    def __str__(self):
        return '%d:%s'%(self.id,self.departmentname)

    class Meta:
        # managed = False
        db_table = 'department'#真映射与数据库表
        #
        verbose_name='部门'
        verbose_name_plural='部门信息管理'
