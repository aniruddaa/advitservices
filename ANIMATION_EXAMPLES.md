<!-- Example: Using Animations in Different Page Sections -->

# Animation Examples for Different Pages

## 1. Home Page (Hero Section)

```html
{% extends "base.html" %}

{% block content %}

<!-- Hero Section with 3D Effects -->
<section class="jumbotron">
    <div class="container text-center">
        <!-- Title with glow and animation -->
        <h1 class="display-4 glow fade-in">Welcome to Advit Placement Services</h1>
        
        <!-- Subtitle with animation -->
        <p class="lead slide-in-right">Find your dream job with our advanced AI Advisor</p>
        
        <!-- Buttons with ripple effect -->
        <div class="mt-5">
            <a href="{% url 'job-list' %}" class="btn btn-primary btn-lg me-3">
                <i class="fas fa-briefcase"></i> Browse Jobs
            </a>
            <a href="{% url 'register' %}" class="btn btn-success btn-lg">
                <i class="fas fa-user-plus"></i> Register Now
            </a>
        </div>
    </div>
</section>

<!-- Features Section -->
<section class="py-5 container">
    <h2 class="text-center mb-5 slide-in-left">Why Choose Us?</h2>
    
    <div class="row">
        <!-- Animated feature cards -->
        <div class="col-md-4 mb-4 slide-in-left">
            <div class="card">
                <div class="card-body text-center">
                    <i class="fas fa-robot fa-3x mb-3" style="color: #007bff;"></i>
                    <h5 class="card-title">AI Advisor</h5>
                    <p class="card-text">Smart recommendations using advanced algorithms</p>
                </div>
            </div>
        </div>
        
        <div class="col-md-4 mb-4 slide-in-right">
            <div class="card">
                <div class="card-body text-center">
                    <i class="fas fa-building fa-3x mb-3" style="color: #28a745;"></i>
                    <h5 class="card-title">Top Companies</h5>
                    <p class="card-text">Opportunities from leading organizations</p>
                </div>
            </div>
        </div>
        
        <div class="col-md-4 mb-4 slide-in-left">
            <div class="card">
                <div class="card-body text-center">
                    <i class="fas fa-lightning-bolt fa-3x mb-3" style="color: #ffc107;"></i>
                    <h5 class="card-title">Quick Matching</h5>
                    <p class="card-text">Fast and accurate job matching in seconds</p>
                </div>
            </div>
        </div>
    </div>
</section>

{% endblock %}
```

## 2. Job Listings Page

```html
{% extends "base.html" %}

{% block content %}

<div class="container mt-5">
    <!-- Search bar with animation -->
    <div class="search-bar slide-in-up">
        <div class="row">
            <div class="col-md-6">
                <input type="text" class="form-control" placeholder="Search jobs...">
            </div>
            <div class="col-md-6">
                <button class="btn btn-primary w-100">Search</button>
            </div>
        </div>
    </div>

    <!-- Job listings with animations -->
    <div class="row mt-5">
        {% for job in jobs %}
        <div class="col-md-6 mb-4 fade-in">
            <div class="card job-card">
                <!-- Job type badge with pulse animation -->
                <div class="card-body">
                    <div class="mb-3">
                        <span class="job-type-badge">{{ job.job_type }}</span>
                    </div>
                    
                    <h5 class="card-title">{{ job.title }}</h5>
                    <p class="card-text">{{ job.description|truncatewords:20 }}</p>
                    
                    <!-- Status badge -->
                    <div class="mb-3">
                        {% if job.is_active %}
                            <span class="status-badge status-reviewing">Open</span>
                        {% else %}
                            <span class="status-badge status-rejected">Closed</span>
                        {% endif %}
                    </div>
                    
                    <!-- Animated button -->
                    <a href="{% url 'job-detail' job.id %}" class="btn btn-primary">
                        View Details
                    </a>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
</div>

{% endblock %}
```

## 3. Company Profile Page

```html
{% extends "base.html" %}

{% block content %}

<!-- Profile header with 3D effect -->
<div class="profile-header">
    <div class="container">
        <div class="row align-items-center">
            <!-- Company logo with 3D rotation -->
            <div class="col-md-3 text-center fade-in">
                <img src="{{ company.logo.url }}" 
                     class="company-logo" 
                     alt="{{ company.name }}"
                     style="width: 200px;">
            </div>
            
            <!-- Company info with animations -->
            <div class="col-md-9 slide-in-right">
                <h1 class="display-4">{{ company.name }}</h1>
                <p class="lead">{{ company.description }}</p>
                
                <div class="mt-3">
                    <a href="{% url 'company-update' %}" class="btn btn-light btn-lg">
                        Edit Profile
                    </a>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Company details with cards -->
<div class="container my-5">
    <div class="row">
        <div class="col-md-4 mb-4 slide-in-left">
            <div class="dashboard-card">
                <div class="card-header">
                    <i class="fas fa-building"></i> Industry
                </div>
                <div class="card-body">
                    {{ company.industry }}
                </div>
            </div>
        </div>
        
        <div class="col-md-4 mb-4 slide-in-right">
            <div class="dashboard-card">
                <div class="card-header">
                    <i class="fas fa-map-marker-alt"></i> Location
                </div>
                <div class="card-body">
                    {{ company.location }}
                </div>
            </div>
        </div>
        
        <div class="col-md-4 mb-4 slide-in-left">
            <div class="dashboard-card">
                <div class="card-header">
                    <i class="fas fa-users"></i> Employees
                </div>
                <div class="card-body">
                    {{ company.employee_count }}
                </div>
            </div>
        </div>
    </div>
</div>

{% endblock %}
```

## 4. User Profile Page

```html
{% extends "base.html" %}

{% block content %}

<!-- Profile header with floating image -->
<div class="profile-header">
    <div class="container">
        <div class="row align-items-center justify-content-center">
            <div class="col-md-8 text-center">
                <!-- Floating profile image -->
                <img src="{{ user.profile.image.url }}" 
                     class="profile-image fade-in"
                     alt="Profile"
                     style="width: 200px; margin-bottom: 20px;">
                
                <!-- User info with animations -->
                <h1 class="display-5 slide-in-down">{{ user.get_full_name }}</h1>
                <p class="lead">{{ user.profile.bio }}</p>
            </div>
        </div>
    </div>
</div>

<!-- Profile stats with counter animation -->
<div class="container my-5">
    <div class="row">
        <div class="col-md-3 text-center mb-4 slide-in-left">
            <div class="card dashboard-card">
                <div class="card-body">
                    <h3 class="counter" data-target="{{ applications.count }}">0</h3>
                    <p class="text-muted">Applications</p>
                </div>
            </div>
        </div>
        
        <div class="col-md-3 text-center mb-4 slide-in-right">
            <div class="card dashboard-card">
                <div class="card-body">
                    <h3 class="counter" data-target="{{ saved_jobs.count }}">0</h3>
                    <p class="text-muted">Saved Jobs</p>
                </div>
            </div>
        </div>
        
        <div class="col-md-3 text-center mb-4 slide-in-left">
            <div class="card dashboard-card">
                <div class="card-body">
                    <h3 class="counter" data-target="{{ profile_views }}">0</h3>
                    <p class="text-muted">Profile Views</p>
                </div>
            </div>
        </div>
        
        <div class="col-md-3 text-center mb-4 slide-in-right">
            <div class="card dashboard-card">
                <div class="card-body">
                    <h3 class="counter" data-target="{{ interviews }}">0</h3>
                    <p class="text-muted">Interviews</p>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Profile sections with animations -->
<div class="container mb-5">
    <div class="row">
        <div class="col-md-6 mb-4 slide-in-left">
            <div class="card">
                <div class="card-header">
                    <i class="fas fa-book"></i> Education
                </div>
                <div class="card-body">
                    {% for edu in user.profile.education_set.all %}
                        <h6>{{ edu.institution }}</h6>
                        <p class="text-muted">{{ edu.degree }} • {{ edu.graduation_year }}</p>
                    {% endfor %}
                </div>
            </div>
        </div>
        
        <div class="col-md-6 mb-4 slide-in-right">
            <div class="card">
                <div class="card-header">
                    <i class="fas fa-briefcase"></i> Experience
                </div>
                <div class="card-body">
                    {% for exp in user.profile.experience_set.all %}
                        <h6>{{ exp.company }}</h6>
                        <p class="text-muted">{{ exp.position }} • {{ exp.duration }}</p>
                    {% endfor %}
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Interests with animated badges -->
<div class="container mb-5">
    <h4 class="mb-4 slide-in-left">Interests</h4>
    <div class="fade-in">
        {% for interest in user.profile.interests.all %}
            <span class="badge badge-primary p-2 m-2" style="background: linear-gradient(135deg, #007bff, #0056b3);">
                <i class="fas fa-tag"></i> {{ interest }}
            </span>
        {% endfor %}
    </div>
</div>

{% endblock %}
```

## 5. Job Application Page

```html
{% extends "base.html" %}

{% block content %}

<div class="container my-5">
    <div class="row">
        <!-- Left column: Job details -->
        <div class="col-md-8 mb-4 slide-in-left">
            <div class="card job-card">
                <div class="card-body">
                    <h1 class="card-title mb-4">{{ job.title }}</h1>
                    
                    <!-- Job info with badges -->
                    <div class="mb-4">
                        <span class="job-type-badge">{{ job.job_type }}</span>
                        {% if job.is_featured %}
                            <span class="status-badge status-reviewing ms-2">Featured</span>
                        {% endif %}
                    </div>
                    
                    <p class="card-text">{{ job.description }}</p>
                    
                    <!-- Requirements with animation -->
                    <h5 class="mt-4 mb-3 slide-in-right">Requirements</h5>
                    <ul class="fade-in">
                        {% for req in job.requirements %}
                            <li>{{ req }}</li>
                        {% endfor %}
                    </ul>
                </div>
            </div>
        </div>
        
        <!-- Right column: Application form -->
        <div class="col-md-4 slide-in-right">
            <div class="card dashboard-card">
                <div class="card-header">
                    Apply for this position
                </div>
                <div class="card-body">
                    <!-- Application form with animated inputs -->
                    <form method="post" class="fade-in">
                        {% csrf_token %}
                        
                        <div class="form-group mb-3">
                            <label for="cover_letter" class="form-label">Cover Letter</label>
                            <textarea name="cover_letter" 
                                      class="form-control" 
                                      rows="5" 
                                      placeholder="Tell us why you're interested..."></textarea>
                        </div>
                        
                        <button type="submit" class="btn btn-success btn-block w-100">
                            <i class="fas fa-paper-plane"></i> Submit Application
                        </button>
                    </form>
                    
                    <!-- Application status -->
                    {% if has_applied %}
                        <div class="alert alert-info mt-3">
                            <i class="fas fa-check-circle"></i>
                            You have already applied for this job
                        </div>
                    {% endif %}
                </div>
            </div>
        </div>
    </div>
</div>

{% endblock %}
```

## 6. Dashboard Page

```html
{% extends "base.html" %}

{% block content %}

<div class="container my-5">
    <!-- Dashboard header -->
    <div class="mb-5 slide-in-down">
        <h1 class="display-4">Your Dashboard</h1>
        <p class="lead text-muted">Welcome back, {{ user.first_name }}!</p>
    </div>

    <!-- Quick stats with counter animation -->
    <div class="row mb-5">
        <div class="col-md-3 mb-4 slide-in-left">
            <div class="dashboard-card text-center">
                <div class="card-body">
                    <h2 class="counter" data-target="{{ active_applications }}">0</h2>
                    <p>Active Applications</p>
                </div>
            </div>
        </div>
        
        <div class="col-md-3 mb-4 slide-in-right">
            <div class="dashboard-card text-center">
                <div class="card-body">
                    <h2 class="counter" data-target="{{ interviews_scheduled }}">0</h2>
                    <p>Interviews Scheduled</p>
                </div>
            </div>
        </div>
        
        <div class="col-md-3 mb-4 slide-in-left">
            <div class="dashboard-card text-center">
                <div class="card-body">
                    <h2 class="counter" data-target="{{ offers_received }}">0</h2>
                    <p>Offers Received</p>
                </div>
            </div>
        </div>
        
        <div class="col-md-3 mb-4 slide-in-right">
            <div class="dashboard-card text-center">
                <div class="card-body">
                    <h2 class="counter" data-target="{{ rejections }}">0</h2>
                    <p>Rejections</p>
                </div>
            </div>
        </div>
    </div>

    <!-- Recent applications -->
    <h3 class="mb-4 slide-in-left">Recent Applications</h3>
    <div class="row mb-5">
        {% for application in recent_applications %}
        <div class="col-md-6 mb-4 fade-in">
            <div class="card job-card">
                <div class="card-body">
                    <h5 class="card-title">{{ application.job.title }}</h5>
                    <p class="card-text">{{ application.job.company.name }}</p>
                    
                    <!-- Status badge -->
                    <span class="status-badge status-{{ application.status|lower }}">
                        {{ application.get_status_display }}
                    </span>
                    
                    <small class="d-block mt-2 text-muted">
                        Applied: {{ application.applied_date|date:"M d, Y" }}
                    </small>
                </div>
            </div>
        </div>
        {% empty %}
        <div class="col-12">
            <div class="alert alert-info">
                <i class="fas fa-info-circle"></i>
                No applications yet. Start applying to jobs!
            </div>
        </div>
        {% endfor %}
    </div>
</div>

{% endblock %}
```

---

## 🎯 Key Points for Implementation

1. **Use fade-in for list items** - Creates smooth, sequential appearance
2. **Use slide-in-left and slide-in-right** - Creates dynamic visual flow
3. **Card elements auto-animate** - No class needed, just use `.card`
4. **Buttons auto-ripple** - Just use `.btn` class
5. **Apply animations to sections** - Not individual elements for better UX
6. **Test on mobile** - Animations should be subtle on small screens

## 📝 Notes

- Animations are GPU-accelerated for smooth 60fps performance
- All animations respect `prefers-reduced-motion` for accessibility
- Use semantic HTML - let CSS handle the styling and animations
- Keep animations under 1 second for UI elements
- Use longer animations (2-3s) for background effects

---

**Ready to use**: Copy-paste these examples into your templates and customize as needed!
