from django.urls import path
from . import views

urlpatterns =[
    path('add/',views.AddView.as_view(),name='dept_add'),
    path('show/',views.ListView.as_view(),name='dept_list'),
    path('update/<int:i>/',views.UpdateView.as_view(),name='update_dept'),
    path('delete/<int:i>/',views.DeleteView.as_view(),name='delete_dept'),
]