from django.db import models


class Menus(models.Model):
    key = models.AutoField(primary_key=True)  # 自增字段，作为主键
    name = models.CharField(max_length=255, null=True)  # 菜单名称
    path = models.CharField(max_length=255, null=True)  # 菜单地址
    menu_type = models.CharField(max_length=255, null=True)  # 菜单类型
    component = models.CharField(max_length=255, null=True)  # 组件
    meta = models.JSONField(null=True)  # 菜单元数据
    parentId = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                               related_name='children')  # 父级菜单id
    redirect = models.CharField(max_length=255, null=True)  # 重定向
    buttons = models.JSONField(null=True) # 按钮
    permission = models.CharField(max_length=255, null=True)
    class Meta:
        db_table = 'menus'
        # 插入数据自定义数据并且只执行一次


    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def get_children(self):
        return Menus.objects.filter(parent_id=self.id)

    def get_children_list(self):
        return Menus.objects.filter(parent_id=self.id).values()

    def get_children_list_recursive(self):
        children = self.get_children()
        children_list = []
        for child in children:
            children_list.append(child)
            children_list.extend(child.get_children_list_recursive())
        return children_list

# Create your models here.
