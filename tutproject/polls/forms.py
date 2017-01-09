from django import forms
from django.contrib.auth.models import User
from polls.models import Question, Choice, ToDo


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('question_text',)


class ChoiceForm(forms.ModelForm):

    class Meta:
        model = Choice
        fields = ('question', 'choice_text', 'votes')


class TodoForm(forms.ModelForm):

    class Meta:
        model = ToDo
        fields = ('todo', 'work')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password')

