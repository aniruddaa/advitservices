import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
import joblib
from pathlib import Path
import os

class CareerAdvisor:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.model_dir = Path(__file__).resolve().parent / 'ml_models'
        self.model_dir.mkdir(exist_ok=True)
        
    def _prepare_profile_features(self, profile):
        """Convert user profile data into feature vector"""
        # Combine relevant profile information with safe access to attributes
        profile_text = f"{getattr(profile, 'skills', '')} {getattr(profile, 'education', '')} {getattr(profile, 'experience', '')} {getattr(profile, 'interests', '')}"
        return profile_text
    
    def _prepare_job_features(self, job):
        """Convert job data into feature vector"""
        job_text = f"{job.title} {job.description} {job.requirements} {job.company.industry}"
        return job_text
    
    def train_job_recommendation_model(self, profiles, jobs):
        """Train the job recommendation model"""
        # Prepare training data
        profile_texts = [self._prepare_profile_features(p) for p in profiles]
        job_texts = [self._prepare_job_features(j) for j in jobs]
        
        # Create and fit vectorizer
        all_texts = profile_texts + job_texts
        self.vectorizer.fit(all_texts)
        
        # Save the vectorizer
        joblib.dump(self.vectorizer, self.model_dir / 'vectorizer.joblib')
    
    def get_job_recommendations(self, user_profile, available_jobs, n_recommendations=5):
        """Get job recommendations for a user profile"""
        if not available_jobs:
            return []
            
        try:
            # Prepare profile and job features
            profile_text = self._prepare_profile_features(user_profile)
            job_texts = [self._prepare_job_features(job) for job in available_jobs]
            
            # Make sure we have non-empty texts
            if not profile_text.strip() or not any(text.strip() for text in job_texts):
                return []
            
            # Fit vectorizer if needed
            all_texts = [profile_text] + job_texts
            self.vectorizer.fit(all_texts)
            
            # Transform texts to vectors
            profile_vector = self.vectorizer.transform([profile_text])
            job_vectors = self.vectorizer.transform(job_texts)
            
            # Calculate similarity scores
            similarities = cosine_similarity(profile_vector, job_vectors)[0]
            
            # Get top N recommendations
            n_recommendations = min(n_recommendations, len(available_jobs))
            top_indices = similarities.argsort()[-n_recommendations:][::-1]
            recommendations = [(available_jobs[i], float(similarities[i])) for i in top_indices]
            
            return recommendations
        except Exception as e:
            print(f"Error in get_job_recommendations: {str(e)}")
            return []
    
    def analyze_skills(self, user_profile, job_market_skills):
        """Analyze user skills and suggest improvements"""
        if not job_market_skills:
            return {'current_skills': [], 'suggested_skills': {}}
            
        user_skills = set(user_profile.skills.lower().split() if user_profile.skills else [])
        market_skills = set(skill.lower() for skill in job_market_skills if skill.strip())
        
        if not market_skills:
            return {'current_skills': list(user_skills), 'suggested_skills': {}}
        
        # Find missing important skills
        missing_skills = market_skills - user_skills
        
        if not missing_skills:
            return {
                'current_skills': list(user_skills),
                'suggested_skills': {}
            }
        
        # Calculate skill relevance scores using TF-IDF
        skill_texts = [' '.join(user_skills) if user_skills else '', ' '.join(market_skills)]
        skill_vectors = self.vectorizer.fit_transform(skill_texts)
        skill_importance = np.squeeze(np.asarray(skill_vectors[1].sum(axis=0)))
        
        # Sort missing skills by importance
        missing_skills_scores = {
            skill: float(skill_importance[self.vectorizer.vocabulary_.get(skill, 0)])
            for skill in missing_skills
        }
        
        return {
            'current_skills': list(user_skills),
            'suggested_skills': dict(sorted(
                missing_skills_scores.items(),
                key=lambda x: x[1],
                reverse=True
            ))
        }
    
    def suggest_career_path(self, user_profile, job_history, market_trends):
        """Suggest career path based on user profile and market trends"""
        # Prepare feature vectors
        profile_features = self._prepare_profile_features(user_profile)
        
        # Create clusters of career paths
        n_clusters = min(5, len(market_trends))
        kmeans = KMeans(n_clusters=n_clusters)
        
        # Combine all text data for vectorization
        all_texts = [profile_features] + [trend['description'] for trend in market_trends]
        vectors = self.vectorizer.fit_transform(all_texts)
        
        # Fit clusters
        kmeans.fit(vectors)
        
        # Find the cluster of the user's profile
        user_cluster = kmeans.predict(vectors[0:1])[0]
        
        # Get relevant career paths from the same cluster
        relevant_trends = [
            trend for i, trend in enumerate(market_trends)
            if kmeans.predict(vectors[i+1:i+2])[0] == user_cluster
        ]
        
        return {
            'current_path': self._identify_current_path(user_profile),
            'suggested_paths': relevant_trends,
            'confidence_scores': self._calculate_path_confidence(vectors[0], relevant_trends)
        }
    
    def _identify_current_path(self, profile):
        """Identify current career path based on profile"""
        # Simple logic to identify current career path
        return profile.current_position if hasattr(profile, 'current_position') else 'Entry Level'
    
    def _calculate_path_confidence(self, profile_vector, career_paths):
        """Calculate confidence scores for suggested career paths"""
        return {
            path['title']: float(np.random.uniform(0.6, 0.95))  # Simplified for demonstration
            for path in career_paths
        }