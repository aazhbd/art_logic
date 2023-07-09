from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.search import index

from wagtailmarkdown.edit_handlers import MarkdownPanel
from wagtailmarkdown.fields import MarkdownField
from wagtailmetadata.models import MetadataPageMixin


class ProjectIndexPage(MetadataPageMixin, Page):
    project_title = models.CharField(max_length=600, blank=True)
    body = MarkdownField(blank=True)
    image = models.ForeignKey('wagtailimages.Image', blank=True, null=True, on_delete=models.PROTECT, related_name='projects_index_image')

    content_panels = Page.content_panels + [
        FieldPanel("project_title", classname="Home title"),
        MarkdownPanel("body"),
        FieldPanel('image', classname="project image"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('project_title'),
        index.SearchField('body'),
    ]


class ProjectPage(MetadataPageMixin, Page):
    project_title = models.CharField(max_length=600, blank=True)
    body = MarkdownField(blank=True)
    image = models.ForeignKey('wagtailimages.Image', blank=True, null=True, on_delete=models.PROTECT, related_name='project_image')

    content_panels = Page.content_panels + [
        FieldPanel("project_title", classname="Home title"),
        MarkdownPanel("body"),
        FieldPanel('image', classname="project image"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('project_title'),
        index.SearchField('body'),
    ]