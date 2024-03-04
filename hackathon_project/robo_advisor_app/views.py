from django.shortcuts import render
from django.views import generic
# from .models import User, Questionnaire, Recommendation, Response

# Create your views here.
from rest_framework.response import Response
from rest_framework import generics, permissions
from .models import *
from .serializers import *

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class QuestionnaireListCreateView(generics.ListCreateAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # Add the recommendation link to the response
        response.data['recommendation_link'] = request.build_absolute_uri(f'/api/questionnaires/{response.data["id"]}/recommendations/')
        return response





class RecommendationListCreateView(generics.ListCreateAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer

class ResponseListCreateView(generics.ListCreateAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer


## fetch list of questionnaires for a particuar user_id
class UserQuestionnaireListView(generics.ListAPIView):
    serializer_class = QuestionnaireSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Questionnaire.objects.filter(user__id=user_id)


# list of Recommendations based on the Questionnaire IDs for a Particular User:
class UserRecommendationListView(generics.ListAPIView):
    serializer_class = RecommendationSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Recommendation.objects.filter(questionnaire__user__id=user_id)



class UserListView(generic.ListView):
    model = User
    template_name = 'users/user_list.html'  # Specify your own template name/location

class UserDetailView(generic.DetailView):
    model = User
    template_name = 'users/user_detail.html'  # Specify your own template name/location

class QuestionnaireListView(generic.ListView):
    model = Questionnaire
    template_name = 'questionnaires/questionnaire_list.html'  # Specify your own template name/location

class QuestionnaireDetailView(generic.DetailView):
    model = Questionnaire
    template_name = 'questionnaires/questionnaire_detail.html'  # Specify your own template name/location

class RecommendationListView(generic.ListView):
    model = Recommendation
    template_name = 'recommendations/recommendation_list.html'  # Specify your own template name/location

class RecommendationDetailView(generic.DetailView):
    model = Recommendation
    template_name = 'recommendations/recommendation_detail.html'  # Specify your own template name/location

class ResponseListView(generic.ListView):
    model = Response
    template_name = 'responses/response_list.html'  # Specify your own template name/location

class ResponseDetailView(generic.DetailView):
    model = Response
    template_name = 'responses/response_detail.html'  # Specify your own template name/location

