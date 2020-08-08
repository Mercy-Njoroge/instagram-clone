from django.db import models

# Create your models here.
class Profile(models.Model):
    pro_picture = models.ImageField(upload_to = 'profile-pics', null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_bio = HTMLField()


    def __str__(self):
        return self.user.username