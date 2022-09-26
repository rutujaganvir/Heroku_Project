from django.urls import path
from .views import Productview,show,updateview,deleteview

urlpatterns=[
    path('laptop/',Productview,name='laptop'),
    path('show/',show,name='show'),
    path('update/<int:id>/',updateview,name='update'),
    path('delete/<int:id>/',deleteview,name='delete'),
]
