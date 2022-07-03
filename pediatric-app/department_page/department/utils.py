from .models import *

menu = [
    {'title': 'Главная', 'url_name': 'index'},
    {'title': 'Расписание', 'url_name': 'timetables'},
    {'title': 'Сотрудники', 'url_name': 'employees'},
    {'title': 'Образование', 'url_name': 'index'},
    {'title': 'МНО', 'url_name': 'index'},

]


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        context['cats'] = cats

        return context
