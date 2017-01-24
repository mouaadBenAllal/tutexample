from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView
from polls.forms import QuestionForm, ChoiceForm, UserForm, TodoForm
from polls.models import Question, Choice, ToDo


def register(request):
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # email
            subject = 'Thank you for registering.'
            message = 'Welcome to ToDo!'
            from_email = settings.EMAIL_HOST_USER
            to_list = [user.email, settings.EMAIL_HOST_USER]

            send_mail(subject, message, from_email, to_list, fail_silently=False)

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print 'user_form.errors'

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render(request, 'register.html',
                  {'user_form': user_form, 'registered': registered})


class QuestionListView(ListView):
    template_name = 'list.html'
    model = Question


class ChoiceListView(ListView):
    template_name = 'choicelist.html'
    model = Choice


class MyView(CreateView):
    form_class = QuestionForm
    template_name = 'question.html'
    success_url = reverse_lazy('listview')


class MyViewUpdate(UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = 'update_question.html'
    success_url = reverse_lazy('listview')


class QuestionDelete(DeleteView):
    model = Question
    template_name = 'delete_question.html'
    success_url = reverse_lazy('listview')


class ChoiceView(CreateView):
    form_class = ChoiceForm
    template_name = 'choice.html'
    success_url = reverse_lazy('choiceview')


    # ---------------------------------------------------------------------


class TodoListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = ToDo
    template_name = 'todolist.html'


class TodoDelete(DeleteView):
    model = ToDo
    success_url = reverse_lazy('todolistview')

    def get_queryset(self):
        queryset = super(TodoDelete, self).get_queryset()
        return queryset.filter(user=self.request.user)


class TodoCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = TodoForm
    template_name = 'todo_create.html'
    success_url = reverse_lazy('todolistview')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoCreateView, self).form_valid(form)


class UpdateToDo(UpdateView):
    model = ToDo
    form_class = TodoForm
    template_name = 'todo_update.html'
    success_url = reverse_lazy('todolistview')

    def get_queryset(self):
        queryset = super(UpdateToDo, self).get_queryset()
        return queryset.filter(user=self.request.user)

