from django import forms
from todo.models import Todo

class TodoForm(forms.ModelForm):
    #설정 정보
    class Meta:
        model = Todo
        fields = ['title', 'description', 'start_date', 'end_date'] #폼에 표시할 필드 지정

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'start_date', 'end_date', 'is_completed']