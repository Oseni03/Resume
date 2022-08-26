from django.shortcuts import render
from django.contrib import messages
from .models import (
  UserProfile, Skills, ContactProfile,
  Testimonial, Portfolio, Blog,
  Certificate)

from django.views import generic

from .forms import ContactForm

# Create your views here.
class IndexView(generic.TemplateView):
  template_name = "resume/index.html"
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    
    blogs = Blog.objects.filter(is_active=True)
    testimonials = Testimonial.objects.filter(is_active=True)
    portfolio = Portfolio.objects.filter(is_active=True)
    certificates = Certificate.objects.filter(is_active=True)
    key_skills = Skills.objects.filter(is_key_skill=True)
    non_key_skills = Skills.objects.filter(is_key_skill=False)
    
    context["blogs"] = blogs
    context["testimonials"] = testimonials
    context["portfolio"] = portfolio
    context["certificates"] = certificates 
    context["key_skills"] = key_skills 
    context["non_key_skills"] = non_key_skills 
    return context


class ContactView(generic.FormView):
  form_class = ContactForm 
  success_url = "/contact/"
  
  def form_valid(self, form):
    contact = form.save(commit=False)
    contact.user = UserProfile.objects.first()
    contact.save()
    messages.success(self.request, "Thank you. We will get in touch with you shortly")
    return super().form_valid(form)
  
  def get_template_names(self):
    if self.request.htmx:
      return "resume/partials/contact-form.html"
    # super().get_template_names()
    return "resume/contact.html"


class PortfolioView(generic.ListView):
  model = Portfolio 
  template_name = "resume/portfolio.html"
  paginate_by = 10 
  context_object_name = "portfolio"
  
  def get_queryset(self):
    return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
  model = Portfolio 
  template_name = "resume/portfolio-detail.html"
  context_object_name = "portfolio"


class BlogView(generic.ListView):
  model = Blog 
  template_name = "resume/blog.html"
  paginate_by = 10 
  context_object_name = "blogs"
  
  def get_queryset(self):
    return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
  model = Blog 
  template_name = "resume/blog-detail.html"
  context_object_name = "blog"