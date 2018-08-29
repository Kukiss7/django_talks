from django.contrib import admin
from django.urls import path
from boards import views

urlpatterns = [
	path('', views.home, name='home'),
	path('boards/<slug:pk>/', views.board_topics, name='board_topics'),
    path('boards/<slug:pk>/new/', views.new_topic, name='new_topic'),
    path('admin/', admin.site.urls)
]
