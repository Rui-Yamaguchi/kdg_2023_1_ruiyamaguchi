from django.urls import path
from . import views

app_name='whitebox'

urlpatterns = [
    path('',views.WhiteboxView,name='index'),
    path('Howaito',views.Howaito,name='Howaito'),
    path('Rio',views.Rio,name='Rio'),
    path('Aka',views.Aka,name='ToudaiAka'),
    path('Tedhi',views.Tedhi,name='Teddy'),
    path('Coco',views.Coco,name='Coco'),
    path('Wiru',views.Wiru,name='Will'),
    path('Communication',views.HelloClass.as_view(),name='index2'),
    path('list/',views.WhiteboxList.as_view(),name='whitebox-list'),
    path('detail/<int:pk>/',views.WhiteboxDetail.as_view(),name='whitebox-detail'),
    path('create/',views.WhiteboxCreate.as_view(),name='whitebox-create'),
    path('delete/<int:pk>',views.WhiteboxDelete.as_view(),name='whitebox-delete'),
    path('update/<int:pk>',views.WhiteboxUpdate.as_view(),name='whitebox-update'),
    path('comment/create/<int:key>',views.CommentCreate.as_view(),name='comment-create'),
]
