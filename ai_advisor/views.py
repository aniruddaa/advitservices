from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .ml_engine import CareerAdvisor
from .models import CareerRecommendation, SkillAnalysis, CareerPath
from jobs.models import Job
from users.models import Profile

advisor = CareerAdvisor()

@login_required
def ai_dashboard(request):
    profile = Profile.objects.get(user=request.user)
    available_jobs = Job.objects.all()
    
    # Initialize recommendations with empty defaults
    context = {
        'recommendations': [],
        'skill_analysis': {'current_skills': [], 'suggested_skills': {}},
        'career_path': {'current_path': 'Entry Level', 'suggested_paths': [], 'confidence_scores': {}}
    }
    
    if not available_jobs:
        messages.warning(request, 'No jobs available in the system yet. Recommendations will be available once jobs are added.')
        return render(request, 'ai_advisor/dashboard.html', context)
    
    # Train the vectorizer with available data
    all_profiles = Profile.objects.all()
    advisor.train_job_recommendation_model(all_profiles, available_jobs)
    
    # Get or create career recommendation
    recommendation, created = CareerRecommendation.objects.get_or_create(
        user_profile=profile,
        defaults={'confidence_score': 0.0}
    )
    
    # Get job recommendations
    try:
        job_recommendations = advisor.get_job_recommendations(profile, available_jobs)
        if job_recommendations:
            recommendation.recommended_jobs.set([job for job, _ in job_recommendations])
            recommendation.confidence_score = sum(score for _, score in job_recommendations) / len(job_recommendations)
            recommendation.save()
    except Exception as e:
        messages.error(request, f'Error generating job recommendations: {str(e)}')
        job_recommendations = []
    
    # Analyze skills
    try:
        job_market_skills = set()
        for job in available_jobs:
            if job.requirements:
                job_market_skills.update(job.requirements.split())
        
        if job_market_skills:
            skill_analysis = advisor.analyze_skills(profile, job_market_skills)
            # Save skill analysis
            SkillAnalysis.objects.create(
                user_profile=profile,
                skills_identified=skill_analysis['current_skills'],
                suggested_skills=skill_analysis['suggested_skills']
            )
        else:
            skill_analysis = {'current_skills': [], 'suggested_skills': {}}
            messages.info(request, 'No job requirements available for skill analysis.')
    except Exception as e:
        messages.error(request, f'Error analyzing skills: {str(e)}')
        skill_analysis = {'current_skills': [], 'suggested_skills': {}}
    
    # Get career path suggestions
    try:
        market_trends = [
            {'title': 'Data Science', 'description': 'Career in data analysis and machine learning'},
            {'title': 'Web Development', 'description': 'Full-stack web development career'},
            {'title': 'Cloud Architecture', 'description': 'Career in cloud computing and infrastructure'},
            {'title': 'Digital Marketing', 'description': 'Career in online marketing and social media'},
            {'title': 'UI/UX Design', 'description': 'Career in user interface and experience design'}
        ]
        
        career_path_suggestion = advisor.suggest_career_path(profile, None, market_trends)
        
        # Save career path
        CareerPath.objects.create(
            user_profile=profile,
            current_path=career_path_suggestion['current_path'],
            suggested_paths=career_path_suggestion['suggested_paths']
        )
    except Exception as e:
        messages.error(request, f'Error generating career path suggestions: {str(e)}')
        career_path_suggestion = {
            'current_path': 'Entry Level',
            'suggested_paths': [],
            'confidence_scores': {}
        }
    
    context = {
        'recommendations': job_recommendations,
        'skill_analysis': skill_analysis,
        'career_path': career_path_suggestion,
    }
    
    return render(request, 'ai_advisor/dashboard.html', context)

@login_required
def update_preferences(request):
    profile = Profile.objects.get(user=request.user)
    
    if request.method == 'POST':
        # Update user preferences for better recommendations
        profile.interests = request.POST.get('interests', '')
        
        # Get additional preferences
        work_environment = request.POST.getlist('work_environment[]', [])
        experience_level = request.POST.get('experience_level', 'entry')
        focus_areas = request.POST.getlist('focus_areas[]', [])
        
        # Store preferences in profile interests field as structured text
        preferences = f"""Career Interests:
{profile.interests}

Work Environment: {', '.join(work_environment)}
Experience Level: {experience_level}
Focus Areas: {', '.join(focus_areas)}"""
        
        profile.interests = preferences
        profile.save()
        
        messages.success(request, 'Your AI advisor preferences have been updated successfully!')
        
    # Get current preferences to pre-fill the form
    current_preferences = {
        'work_environment': [],
        'experience_level': 'entry',
        'focus_areas': []
    }
    
    if profile.interests:
        try:
            # Try to parse existing preferences
            lines = profile.interests.split('\n')
            for line in lines:
                if 'Work Environment:' in line:
                    current_preferences['work_environment'] = [env.strip() for env in line.split(':')[1].strip().split(',')]
                elif 'Experience Level:' in line:
                    current_preferences['experience_level'] = line.split(':')[1].strip()
                elif 'Focus Areas:' in line:
                    current_preferences['focus_areas'] = [area.strip() for area in line.split(':')[1].strip().split(',')]
        except Exception:
            # If parsing fails, keep defaults
            pass
    
    context = {
        'preferences': current_preferences,
        'interests': profile.interests.split('\n\n')[0].replace('Career Interests:\n', '') if profile.interests else ''
    }
    
    return render(request, 'ai_advisor/preferences.html', context)