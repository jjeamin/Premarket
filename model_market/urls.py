from django.urls import path
from model_market.views import *

app_name = 'mm'
urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    # path('task/', TaskTemplateView.as_view(), name='task_list'),
    # path('framework/', FrameworkTemplateView.as_view(), name='framework_list'),
    path('framework/<int:pk>', FrameWorkDetailView.as_view(), name='framework_detail'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('model/<int:pk>/', ModelDetailView.as_view(), name='model_detail'),
    path('add/', ModelCreateView.as_view(), name='model_create'),
    path('change/', ModelChangeView.as_view(), name='model_change'),
    path('<int:pk>/model_update/', ModelUpdateView.as_view(), name='model_update'),
    path('<int:pk>/model_delete/', ModelDeleteView.as_view(), name='model_delete'),
]