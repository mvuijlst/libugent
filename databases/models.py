from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.core.models import Page
from core.models import ContentPage


class DatabasesIndexPage(Page):
    """Index page for databases section"""
    parent_page_types = ['home.HomePage']
    subpage_types = ['databases.DatabasePage']
    
    class Meta:
        verbose_name = _('Databases Index Page')
        
    def get_context(self, request):
        context = super().get_context(request)
        # Add database pages to the context
        context['database_pages'] = DatabasePage.objects.child_of(self).live().order_by('title')
        return context


class DatabasePage(ContentPage):
    """Page for a specific database"""
    parent_page_types = ['databases.DatabasesIndexPage']
    
    class Meta:
        verbose_name = _('Database Page')
