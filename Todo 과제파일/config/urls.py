from django.contrib import admin
from django.urls import path, include

from todo.views import todo_list, todo_info
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('bookmark/', views.bookmark_list),
    # path('bookmark/<int:pk>', views.bookmark_detail),

    path('todo/', todo_list, name='todo_list'),
    path('todo/<int:todo_id>/', todo_info, name='todo_info'),
    path('accounts', include('django.contrib.auth.urls')),
    path('accounts/login/', user_views.login, name='login'),
    path('accounts/signup/', user_views.sign_up, name='signup'),
]
