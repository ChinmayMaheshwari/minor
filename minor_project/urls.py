from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from . import views

app_name='minor_project'

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('feature/',views.feature,name='feature'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path('register/',views.register,name='register'),
	path('login/',views.user_login,name='user_login'),
	path('logout/',views.user_logout,name='logout'),
    path('recorder/<int:pk>/',views.upload_file,name='upload_file'),
    path('result/<int:interview_number>',views.result,name='result'),
    ]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 