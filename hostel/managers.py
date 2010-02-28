from django.contrib.sites.models import Site
from django.db import models


class QSManager(models.Manager):

    use_for_related_fields = True
    def __init__(self, qs_class=models.query.QuerySet):
        super(QSManager, self).__init__()
        self.queryset_class = qs_class

    def get_query_set(self):
        return self.queryset_class(self.model)

    def __getattr__(self, attr, *args):
        try:
            return getattr(self.__class__, attr, *args)
        except AttributeError:
            return getattr(self.get_query_set(), attr, *args)


class QuerySet(models.query.QuerySet):

    """
    Default implementation of models.Manager.get_query_set is simply

    ... return QuerySet(self.model)

    as_manager returns a Manager class that can return a custom QuerySet
    instance

    ... return self.queryset_class(self.model)
    """

    @classmethod
    def as_manager(cls, ManagerClass=QSManager):
        return ManagerClass(cls)

    def first(self):
        return self[0]

    def on_site(self):
        return self.filter(site=Site.objects.get_current())
