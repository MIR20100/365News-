from django.db.models import Manager

class CategoryManager(Manager):
    def get_category(self, category_name):
        try:
            return self.get(name__icontains = category_name)
        except Exception:
            return None