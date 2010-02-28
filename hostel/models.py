from django.db import models
from django.utils.safestring import mark_safe


_field_name = lambda name: '%s_rendered' % name
class MarkdownField(models.TextField):


    def contribute_to_class(self, cls, name):
        field_name = '%s_rendered' % name
        field_as_html_name = '%s_html' % name
        field = models.TextField(editable=False)
        cls.add_to_class(field_name, field)
        super(MarkdownField, self).contribute_to_class(cls, name)

        def as_html(self):
            return mark_safe(getattr(self, field_name))
        cls.add_to_class(field_as_html_name, property(as_html))

    def pre_save(self, model_instance, add):
        import markdown
        markup = getattr(model_instance, self.attname)
        rendered = markdown.markdown(markup, safe_mode='remove')
        setattr(model_instance, _field_name(self.attname), rendered)
        return markup
