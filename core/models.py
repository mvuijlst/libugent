from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock as WagtailTableBlock
from django.utils.translation import gettext_lazy as _

class ButtonBlock(blocks.StructBlock):
    """Block for a button with text and link"""
    text = blocks.CharBlock(required=True, help_text=_("Button text"))
    link = blocks.URLBlock(required=True, help_text=_("Button link"))
    
    class Meta:
        template = 'blocks/button_block.html'
        icon = 'link'
        label = _('Button')

class TableBlock(WagtailTableBlock):
    """Enhanced table block with header option"""
    class Meta:
        template = 'blocks/table_block.html'
        icon = 'table'
        label = _('Table')

class BasePage(Page):
    """Abstract base page with common fields"""
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('Featured image for SEO and sharing')
    )
    
    promote_panels = Page.promote_panels + [
        ImageChooserPanel('featured_image'),
    ]
    
    class Meta:
        abstract = True

class ContentPage(BasePage):
    """Generic content page with streamfield content"""
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('document', DocumentChooserBlock()),
        ('embed', EmbedBlock()),
        ('quote', blocks.BlockQuoteBlock()),
        ('html', blocks.RawHTMLBlock()),
        ('button', ButtonBlock()),
        ('table', TableBlock()),
        ('hr', blocks.StaticBlock(template='blocks/hr_block.html')),
    ], null=True, blank=True)
    
    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
    
    class Meta:
        abstract = True
