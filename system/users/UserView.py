from django.views.generic import View
from libs.JsonResponse import ReTurn200
from system.models import Menus
import json

class UserView(View):

    def get(self, request):
        """
        获取用户信息
        :param request:
        :return:
        """
        # 获取所有顶级菜单项（parentId为空）
        root_menus = Menus.objects.filter(parentId__isnull=True).prefetch_related('children')

        # 递归函数，用于构建树形结构
        def build_tree(menus):
            tree = []
            for menu in menus:
                node = {
                    'key': menu.key,
                    'name': menu.name,
                    'path': menu.path,
                    'menu_type': menu.menu_type,
                    'component': menu.component,
                    'meta': menu.meta,
                    'redirect': menu.redirect,
                    'buttons': menu.buttons,
                    'permission': menu.permission,
                    'children': build_tree(menu.children.all())  # 递归获取子菜单
                }
                tree.append(node)
            return tree

        # 构建树形结构
        menu_tree = build_tree(root_menus)

        # 返回 JSON 响应
        return ReTurn200(menu_tree)

    def post(self, request):
        menu_data = json.loads(request.body)
        if menu_data.get('key') == 99999:
            parentId = Menus.objects.get(key=menu_data.get('parentId'))
            # 删除父级菜单
            menu_data.pop('parentId', None)
            # 删除key值
            menu_data.pop('key', None)
            new_menu = Menus.objects.create(**menu_data)
            new_menu.parentId_id = parentId
        else:
            menu_data.pop('children', None)
            Menus.objects.filter(key=menu_data.get('key')).update(**menu_data)
        return ReTurn200({})