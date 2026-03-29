from django.contrib import admin
from django.urls import path, include

from todo.views import todo_list, todo_info, todo_create, todo_delete, todo_update
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('bookmark/', views.bookmark_list),
    # path('bookmark/<int:pk>', views.bookmark_detail),

    path('todo/', todo_list, name='todo_list'),
    path('todo/<int:todo_id>/', todo_info, name='todo_info'),
    path('todo/create/', todo_create, name='todo_create'),
    path('todo/<int:todo_id>/update/', todo_update, name='todo_update'),
    path('todo/<int:todo_id>/delete/', todo_delete, name='todo_delete'),



    #auth
    path('accounts', include('django.contrib.auth.urls')),
    #Django 기본 인증 URL들을 accounts/ 아래에 한 번에 등록하는기능
    path('accounts/login/', user_views.login, name='login'),
    path('accounts/signup/', user_views.sign_up, name='signup'),
]
