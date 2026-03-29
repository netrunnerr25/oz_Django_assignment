from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

from todo.models import Todo
from todo.forms import TodoForm, TodoUpdateForm

@login_required()
def todo_list(request):
    todo_list = Todo.objects.filter(user=request.user).order_by('-created_at')
    # result = [{'id': todo[0], 'title': todo[1]} for i, todo in enumerate(todo_list)]

    #다중 조건 검색을 위해 Q 객체사용하기
    q = request.GET.get('q')
    if q:
        todo_list = todo_list.filter(
            Q(title__contains=q) |
            Q(description__contains=q)
        )

    #페이지네이션 기능
    paginator = Paginator(todo_list, 10) #10개씩 보여주기
    page = request.GET.get('page') #URL 파라미터 꺼내기
    page_obj = paginator.get_page(page) #paginator에서 해당 페이지 번호에 맞는 데이터를 가져옴

    context = {
        # 'date' : result,
        'page_obj' : page_obj,
    }

    return render(request, 'todo/todo_list.html', context)

@login_required()
def todo_info(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    context = {
        'todo' : todo.__dict__, #모든 필드 딕셔너리로 변환
    }
    return render(request, 'todo/todo_info.html', context)

    # try:
    #     todo = Todo.objects.get(id=todo_id) #장고에서 pk/id 자동해석
    #     info = {
    #         'title': todo.title,
    #         'description': todo.description,
    #         'start_date': todo.start_date,
    #         'end_date': todo.end_date,
    #         'is_completed': todo.is_completed
    #     }
    #     return render(request, 'todo/todo_info.html', {'data': info})
    # except Todo.DoesNotExist:
    #     raise Http404("Todo does not exist")

#생성
@login_required()
def todo_create(request):

    #form 사용하기
    form = TodoForm(request.POST or None)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()
        return redirect(reverse('todo_info', kwargs={'todo_id':todo.pk}))
    context = {'form' : form}
    return render (request, 'todo/todo_create.html', context)

#수정
@login_required()
def todo_update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id, user=request.user)

    form = TodoUpdateForm(request.POST or None, instance=todo)
    if form.is_valid():
        todo = form.save()

        return redirect(reverse('todo_info', kwargs={'todo_id': todo.pk}))

    context = {
        'form' : form,
    }
    return render(request, 'todo/todo_update.html', context)

#삭제
@login_required()
def todo_delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id, user=request.user)
    todo.delete()

    return redirect(reverse('todo_list'))