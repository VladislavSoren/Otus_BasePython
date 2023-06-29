from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Project(models.Model):
    class Status(models.IntegerChoices):
        ARCHIVED = 0
        AVAILABLE = 1

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="projects",
    )  # Если удалим Category, то Project не дропнится
    status = models.IntegerField(
        choices=Status.choices
    )

    # new fields
    url = models.CharField(max_length=150, null=True)
    other_contributors = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Product <№{self.id}, {self.name!r}>"


# from shop_projects_app.models import Category
class Creator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField()

    projects = models.ForeignKey(Project, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f"Author {self.user}>"
