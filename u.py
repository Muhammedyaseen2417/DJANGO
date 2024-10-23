from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func',views.func),
    path('fun1/<a>',views.fun1),
    path('task/<int:salary>/<int:year>',views.task),
    path('task1/<city>',views.task1),
    path('task2/<int:num>',views.task2),
    path('task3/<day>',views.task3),
    path('task4/<int:cost>',views.task4),
    path('task5/<int:unit>',views.task5),


]
