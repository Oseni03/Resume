from django.contrib import admin
from .models import (
  UserProfile, Skills, ContactProfile,
  Testimonial, Portfolio, Blog,
  Certificate, Media)

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
  list_display = ("id", "user")
  
@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
  list_display = ("id", "name", "score")
  
@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
  list_display = ("id", "name", "timestamp")
  
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
  list_display = ("id", "name", "is_active")
  
@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
  list_display = ("id", "name", "is_image")
  
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
  list_display = ("id", "date", "name", "is_active")
  readonly_fields = ("slug",)
  
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
  list_display = ("id", "date", "name", "is_active")
  readonly_fields = ("slug",)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
  list_display = ("id", "date", "name", "title")