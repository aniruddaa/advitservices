from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # use a path under the upload folder so MEDIA_ROOT/profile_pics/default.jpg is the expected location
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    resume = models.FileField(upload_to='resumes', blank=True)
    skills = models.TextField(blank=True)
    education = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    interests = models.TextField(blank=True, help_text='Enter your career interests and goals')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # Resize the image only if the file actually exists on disk (guard against missing default file)
        try:
            if self.image and hasattr(self.image, 'path') and os.path.exists(self.image.path):
                img = Image.open(self.image.path)
                if img.height > 300 or img.width > 300:
                    output_size = (300, 300)
                    img.thumbnail(output_size)
                    img.save(self.image.path)
        except (FileNotFoundError, OSError):
            # If the image file is missing or unreadable, skip processing silently.
            pass
