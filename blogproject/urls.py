
from django.contrib import admin
from django.urls import path, include
from blogview import views


urlpatterns = [
     path('admin/', admin.site.urls),
    # path('',views.home),
    # path('learn_django/', views.learn_django ),
    # path('learn_markup/', views.learn_markup ),
    # path('learn_var/', views.learn_var ),
    # path('learn_math/', views.learn_math ),
    path('cor/', include('course.urls')),

]
