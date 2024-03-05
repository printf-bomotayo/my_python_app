"""
URL configuration for hackathon_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from robo_advisor_app.views import * 


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/users/', UserCreateView.as_view(), name='user_create'),

    path('api/users/', UserListCreateView.as_view(), name='user_list'),

    path('api/login/', LoginView.as_view(), name='login'),

    path('api/users/<int:user_id>/questionnaires/', UserQuestionnaireListView.as_view(), name='user_questionnaires'),

    path('api/questionnaires/', QuestionnaireListCreateView.as_view(), name='user_list'),
    
    path('api/recommendations/', RecommendationListCreateView.as_view(), name='user_list'),

    path('api/users/<int:user_id>/recommendations/', UserRecommendationListView.as_view(), name='user_recommendations'),
    
    path('api/responses/', ResponseListCreateView.as_view(), name='user_list'),

    path('users/', UserListView.as_view(), name='user_list'),

    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),

    path('questionnaires/', QuestionnaireListView.as_view(), name='questionnaire_list'),

    path('questionnaires/<int:pk>/', QuestionnaireDetailView.as_view(), name='questionnaire_detail'),

    path('recommendations/', RecommendationListView.as_view(), name='recommendation_list'),

    path('recommendations/<int:pk>/', RecommendationDetailView.as_view(), name='recommendation_detail'),

    path('responses/', ResponseListView.as_view(), name='response_list'),

    path('responses/<int:pk>/', ResponseDetailView.as_view(), name='response_detail'),
]
