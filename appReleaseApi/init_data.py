from system.models import Menus
from django.shortcuts import HttpResponse

def init_data(request):
    initialize_user_data() # 初始化菜单数据

    return HttpResponse("初始化成功")

def initialize_user_data(**kwargs):
    # 当 User 实例首次被创建时，执行以下代码
    if Menus.objects.count() == 0:
        menus_init_data = {
            "path": "/",
            "name": "平台",
            "types": "menu",
            "redirect": "/home",
            "component": "layout",
            "meta": {
                "keepAlive": True
            },
            "buttons": []
        }
        Menus.objects.create(**menus_init_data)
