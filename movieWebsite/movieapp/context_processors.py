from .models import Category
from django.contrib.auth.models import User

def menu_links(request):
    links=Category.objects.all()
    return dict(links=links)

# def user_links(request):
#     user=User.objects.all()
#     return dict(user=user)