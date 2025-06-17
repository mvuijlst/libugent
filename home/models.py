from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BasePage


class HomePage(BasePage):
    """Home page model - only allows creation of DatabasesIndexPage and InfoIndexPage as children"""
    subpage_types = ['databases.DatabasesIndexPage', 'info.InfoIndexPage']
    
    class Meta:
        verbose_name = _('Home Page')
