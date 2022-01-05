from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import CreateUserForm, EditProfileForm
from .models import Post

# Create your views here.

def index(request):
    return render(request, 'blog/home.html')


def password_success(request):
    return render(request, 'registration/password_success.html', {})


class SignUp(CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy("login")
    template_name = "blog/signup.html"


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('blog:password-success')



class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy("blog:home")
    
    def get_object(self):
        return self.request.user



class PostListView(ListView):
    model = Post
    paginate_by = 6
    context_object_name = 'posts'
    


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'


class MyPostsView(ListView):
    model = Post
    paginate_by = 6
    template_name = 'blog/my_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(Q(author=self.request.user))


class CreatePostView(CreateView):
    model = Post 
    fields = ('title','body', 'header')

    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeletePostView(DeleteView):
    model = Post
    context_object_name = 'post'

    success_url = reverse_lazy('blog:my-posts')


class UpdatePostView(UpdateView):
    model = Post
    template_name_suffix = '_update_form'
    context_object_name = 'post'

    fields = ['title','body']