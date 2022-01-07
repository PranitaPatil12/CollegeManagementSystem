from django.urls import path
from . import views

urlpatterns =[
    path('add/',views.AddView.as_view(),name='stud_add'),
    path('show/',views.ListView.as_view(),name='stud_list'),
    path('update/<int:i>/',views.UpdateView.as_view(),name='update_stud'),
    path('delete/<int:i>/',views.DeleteView.as_view(),name='delete_stud'),
]