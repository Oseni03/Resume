from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from PIL import Image

# Create your models here.
class UserProfile(models.Model):
  class Meta:
    verbose_name_plural = "User Profiles"
    verbose_name = "User Profile"
  
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
  title = models.CharField(max_length=200, null=True, blank=True)
  bio = models.TextField(blank=True, null=True)
  cv = models.FileField(blank=True, null=True, upload_to="cv")
  
  def __str__(self):
    return f"{self.user.first_name} {self.user.last_name}"
  
  # def save(self, *args, **kwargs):
  #   super().save(*args, **kwargs)
  #   img = Image.open(self.image.path)
    
  #   if img.heigth > 300 or img.width > 300:
  #     output_size = (300,300)
  #     img.thumbnail(output_size)
  #     img.save(self.image.path)


class Skills(models.Model):
  class Meta:
    verbose_name_plural = "Skills"
    verbose_name = "Skill"
  
  name = models.CharField(max_length=20, null=True, blank=True)
  score = models.IntegerField(default=80, null=True, blank=True)
  image = models.FileField(blank=True, null=True, upload_to="skills")
  is_key_skill = models.BooleanField(default=False)
  user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True)
  
  def __str__(self):
    return self.name


class ContactProfile(models.Model):
  class Meta:
    verbose_name_plural = "Contact Profiles"
    verbose_name = "Contact Profile"
    ordering = ["timestamp"]
    
  timestamp = models.DateTimeField(auto_now_add=True)
  name = models.CharField(verbose_name="Name", max_length=100)
  email = models.CharField(max_length=150, verbose_name="Email")
  message = models.TextField(verbose_name="Message")
  user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True)
  
  def __str__(self):
    return self.name


class Testimonial(models.Model):
  class Meta:
    verbose_name_plural = "Testimonials"
    verbose_name = "Testimonial"
    ordering = ["name"]
  
  thumbnail = models.ImageField(blank=True, null=True, upload_to="testimonial")
  name = models.CharField(max_length=200, null=True, blank=True)
  role = models.CharField(max_length=200, null=True, blank=True)
  quote = models.CharField(max_length=500, null=True, blank=True)
  is_active = models.BooleanField(default=True)
  user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True)
  
  def __str__(self):
    return self.name


class Media(models.Model):
  class Meta:
    verbose_name_plural = "Media Files"
    verbose_name = "Media"
    ordering = ["name"]
  
  image = models.ImageField(blank=True, null=True, upload_to="media")
  url = models.URLField(null=True, blank=True)
  name = models.CharField(max_length=200, null=True, blank=True)
  is_image = models.BooleanField(default=True)
  user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True)
  
  def save(self, *args, **kwargs):
    if self.url:
      self.is_image = False 
    super(Media, self).save(*args, **kwargs)
  
  def __str__(self):
    return self.name 


class Portfolio(models.Model):
  class Meta:
    verbose_name_plural = "Portfolio Profiles"
    verbose_name = "Portfolio"
    ordering = ["name"]
    
  date = models.DateTimeField(blank=True, null=True)
  name = models.CharField(max_length=200, blank=True, null=True)
  description = models.CharField(max_length=500, blank=True, null=True)
  body = RichTextField(blank=True, null=True)
  image = models.ImageField(blank=True, null=True, upload_to="portfolio")
  slug = models.SlugField(blank=True, null=True)
  is_active = models.BooleanField(default=True)
  user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True)
  
  def save(self, *args, **kwargs):
    if not self.id:
      self.slug = slugify(self.name) 
    super(Portfolio, self).save(*args, **kwargs)
  
  def get_absolute_url(self):
    return f"/portfolio/{self.slug}"
  
  def __str__(self):
    return self.name 


class Blog(models.Model):
  class Meta:
    verbose_name_plural = "Blogs"
    verbose_name = "Blog"
    ordering = ["name"]
    
  date = models.DateTimeField(blank=True, null=True)
  author = models.CharField(max_length=200, blank=True, null=True)
  name = models.CharField(max_length=200, blank=True, null=True)
  description = models.CharField(max_length=500, blank=True, null=True)
  body = RichTextField(blank=True, null=True)
  image = models.ImageField(blank=True, null=True, upload_to="blog")
  slug = models.SlugField(blank=True, null=True)
  is_active = models.BooleanField(default=True)
  user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True)
  
  def save(self, *args, **kwargs):
    if not self.id:
      self.slug = slugify(self.name) 
    super(Blog, self).save(*args, **kwargs)
  
  def get_absolute_url(self):
    return f"/blog/{self.slug}"
  
  def __str__(self):
    return self.name 


class Certificate(models.Model):
  class Meta:
    verbose_name_plural = "Certicates"
    verbose_name = "Certificate"
    ordering = ["name"]
    
  date = models.DateTimeField(blank=True, null=True)
  title = models.CharField(max_length=50, blank=True, null=True)
  name = models.CharField(max_length=200, blank=True, null=True)
  description = models.CharField(max_length=500, blank=True, null=True)
  is_active = models.BooleanField(default=True)
  user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True)
  
  def __str__(self):
    return self.name 