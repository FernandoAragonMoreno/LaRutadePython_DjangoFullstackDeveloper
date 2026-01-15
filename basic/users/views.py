from django.shortcuts import render

from users.models import UserProfile

# Create your views here.
def user_list(request):
    get_all_users = UserProfile.objects.all()
    data = {
        'users': get_all_users
    }
    return render(request, 'users_list.html', data)