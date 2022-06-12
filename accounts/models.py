from django.db import models
from django.contrib.auth.models import User
from .util import generate_ref_code
from django.core.validators import MinValueValidator, MaxValueValidator



class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)



class Refer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #bio = models.TextField(blank=True)
    code = models.CharField(max_length=12,blank=True, default="", null=True)
    is_activated = models.BooleanField(default=False)
    recommended_by = models.ForeignKey(User, on_delete= models.CASCADE, blank=True, null=True, related_name= 'ref_by')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return f"{self.user.username}-{self.code}"
    def get_recommened_profiles(self):
        qs = Refer.objects.all()
        # my_recs = [p for p in qs if p.recommended_by == self.user]

        my_recs = []
        for profile in qs:
            if profile.recommended_by == self.user:
                my_recs.append(profile)
        return my_recs

    def save(self, *args, **kwargs):
        if str(self.code) =='None' or str(self.code) =='':
            self.code = generate_ref_code()
        print("self********** code", self.code)
        #super(*args, **kwargs).save()
        super(Refer, self).save(*args, **kwargs)
