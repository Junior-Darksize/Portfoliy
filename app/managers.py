from django.db.models import Manager


class FeatureManager(Manager):

    def hammasi(self):
        return self.get_queryset()
