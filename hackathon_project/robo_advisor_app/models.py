from django.db import models
from .services import AiService

# Create user object 
class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    password = models.CharField(max_length=128)  # Store hashed passwords

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# create questionnaire object
class Questionnaire(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questionnaires")
    age = models.PositiveIntegerField()
    investment_purpose = models.CharField(max_length=100)
    investment_knowledge = models.CharField(max_length=100)
    investment_horizon = models.CharField(max_length=100)
    risk_tolerance = models.CharField(max_length=100)
    amount = models.FloatField()
    currency = models.CharField(max_length=10)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"Questionnaire {self.id}"


# create recommendation object
class Recommendation(models.Model):
    questionnaire = models.OneToOneField(Questionnaire, on_delete=models.CASCADE)
    response = models.ManyToManyField("Response")

    def __str__(self):
        return f"Recommendation for Questionnaire {self.questionnaire.id}"
    

    def create_recommendations(self):
        ai_service = AiService()
        recommendations = ai_service.get_recommendations(self.questionnaire)
        # Parse the AI response and create Response objects
        for rec in recommendations:
            response = Response.objects.create(**rec)
            self.responses.add(response)
        self.save()


# create recommendation object
class Response(models.Model):
    id = models.AutoField(primary_key=True)
    financial_product = models.TextField(max_length=200)
    ticker = models.TextField(max_length=200)
    provider = models.TextField(max_length=200)
    brief_description = models.TextField(max_length=500)
    expected_return = models.TextField(max_length=200)
    composition = models.TextField(max_length=200)

    def __str__(self):
        return f"Response {self.id}"
