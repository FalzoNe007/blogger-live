from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


app_name = 'blog'
urlpatterns = [
    path('', views.index, name='home'),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('edit_profile/', views.UserEditView.as_view(), name='user-edit'),
    path('password/', views.PasswordsChangeView.as_view(
        template_name='registration/change_password.html')),
    path('password_success', views.password_success, name='password-success'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('myposts/',  login_required(views.MyPostsView.as_view()), name='my-posts'),
    path('posts/create/', login_required(views.CreatePostView.as_view()),
         name='post-create'),
    path('posts/delete/<int:pk>/', login_required(views.DeletePostView.as_view()),
         name='post-delete'),
    path('posts/update/<int:pk>/',
         login_required(views.UpdatePostView.as_view()), name='post-update'),



]
