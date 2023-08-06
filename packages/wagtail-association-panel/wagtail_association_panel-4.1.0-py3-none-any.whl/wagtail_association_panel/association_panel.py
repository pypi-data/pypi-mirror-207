from django.template.loader import render_to_string
from django.db.models.fields.related_descriptors import ForwardManyToOneDescriptor

from modelcluster.fields import ParentalKey

from wagtail.admin.panels import Panel
from wagtail.snippets.models import get_snippet_models

from .apps import get_app_label

__all__ = ['AssociationPanel']


class AssociationPanel(Panel):

    # noinspection SpellCheckingInspection
    def __init__(self, relation_name, heading='', classname='', help_text='', edit_url_name=None):

        super().__init__(heading=heading, classname=classname, help_text=help_text)

        self.edit_url_type = ''
        self.edit_url_name = edit_url_name

        self.relation_name = relation_name
        self.relation = None
        self.relation_model = None
        self.related_model = None
        self.related_model_name_in_relation = ''
        self.related_model_column_in_relation = ''
        self.model = None
        self.model_name_in_relation = ''
        self.model_column_in_relation = ''

        self.instance = None
        self.form = None
        self.request = None

    def clone(self):

        return self.__class__(
            self.relation_name,
            heading=self.heading,
            classname=self.classname,
            help_text=self.help_text,
            edit_url_name=self.edit_url_name,
        )

    def on_model_bound(self):
        manager = getattr(self.model, self.relation_name)
        self.relation = manager.rel
        self.relation_model = self.relation.related_model
        self.name_in_relation = self.relation.field.name
        self.column_in_relation = self.relation.field.column

        self.related_model = None
        self.related_model_name_in_relation = ''
        self.related_model_column_in_relation = ''

        self.edit_url_type = ''

        for attribute in vars(self.relation_model).keys():

            value = getattr(self.relation_model, attribute)

            if not isinstance(value, ForwardManyToOneDescriptor):
                continue

            if not isinstance(value.field, ParentalKey):
               continue

            self.related_model = value.field.related_model
            self.related_model_name_in_relation = value.field.name
            self.related_model_column_in_relation = value.field.column

            if self.related_model in get_snippet_models():
                self.edit_url_type = 'snippet'

            break

    class BoundPanel(Panel.BoundPanel):

        template_name = get_app_label() + "/association_panel.html"

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.instance_associations = list(self.load_associations())

        def load_associations(self):

            kwargs = {self.panel.column_in_relation: self.instance.id}

            associations = self.panel.relation_model.objects.filter(**kwargs).values_list(
                self.panel.related_model_name_in_relation)

            associations = self.panel.related_model.objects.filter(id__in=associations)
            return associations

        def get_context_data(self, parent_context=None):
            context = super().get_context_data(parent_context)

            context['related_model_app_label'] = self.panel.related_model._meta.app_label # noqa
            context['related_model_name'] = self.panel.related_model._meta.model_name # noqa
            context['edit_url_type'] = self.panel.edit_url_type
            context['edit_url_name'] = self.panel.edit_url_name

            return context
