from django.db import models
from users.models import Profile
from jobs.models import Job

class CareerRecommendation(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    recommended_jobs = models.ManyToManyField(Job)
    recommendation_date = models.DateTimeField(auto_now_add=True)
    confidence_score = models.FloatField()
    
    def __str__(self):
        return f"Career Recommendation for {self.user_profile.user.username}"

class SkillAnalysis(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    analysis_date = models.DateTimeField(auto_now_add=True)
    skills_identified = models.JSONField()  # Store identified skills and their confidence scores
    suggested_skills = models.JSONField()  # Store skills to learn
    
    def __str__(self):
        return f"Skill Analysis for {self.user_profile.user.username}"

class CareerPath(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    current_path = models.CharField(max_length=100)
    suggested_paths = models.JSONField()  # Store potential career paths
    path_analysis_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Career Path for {self.user_profile.user.username}"