# Advit Placement Services

A sophisticated job placement platform built with Django, featuring AI-powered job recommendations and career guidance.

## Features

- 👥 User Authentication & Profile Management
- 💼 Job Listings & Applications
- 🏢 Company Profiles
- 🤖 AI-Powered Career Advisor
  - Job Recommendations
  - Skill Analysis
  - Career Path Guidance
- 📊 Dashboard Interface
- 🎯 Personalized Preferences

## Tech Stack

- Django 5.2.7
- Python 3.11.3
- Bootstrap 5
- SQLite Database
- scikit-learn (for AI features)
- Crispy Forms with Bootstrap 4

## Setup

1. Clone the repository:
```bash
git clone https://github.com/aniruddaa/advitservices.git
cd advitservices
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to see the application.

## Project Structure

```
advitplacementservices/
├── advit_placement/      # Main project settings
├── ai_advisor/           # AI recommendation system
├── company/             # Company management
├── core/               # Core functionality
├── jobs/              # Job listings and applications
├── users/             # User authentication and profiles
├── static/            # Static files (CSS, JS)
├── templates/         # HTML templates
└── media/            # User-uploaded content
```

## AI Advisor Features

- Smart job matching using TF-IDF vectorization
- Skill gap analysis and recommendations
- Career path suggestions based on profile
- Personalized learning recommendations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- Anirudda
- GitHub: [@aniruddaa](https://github.com/aniruddaa)

## Acknowledgments

- Django Framework
- Bootstrap Team
- scikit-learn