from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.core.models import Page
from core.models import ContentPage


class InfoIndexPage(Page):
    """Index page for information section"""
    parent_page_types = ['home.HomePage']
    subpage_types = ['info.InfoPage']
    
    class Meta:
        verbose_name = _('Information Index Page')
        
    def get_context(self, request):
        context = super().get_context(request)
        # Add info pages to the context
        context['info_pages'] = InfoPage.objects.child_of(self).live().order_by('title')
        return context


class InfoPage(ContentPage):
    """Page for specific information"""
    parent_page_types = ['info.InfoIndexPage']
    
    class Meta:
        verbose_name = _('Information Page')
