from django.db import models

# Create your models here.

class UserData(models.Model):
    user_id = models.TextField(primary_key=True)
    skill_score = models.FloatField(null=True)
    state = models.CharField(max_length=8, null=True)
    answer = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"user_id: {self.user_id}, skill_score: {self.skill_score}, state: {self.state}, answer: {self.answer}"
