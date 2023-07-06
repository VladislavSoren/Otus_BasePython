from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):  # base class should subclass 'django.db.models.Model'

    class Status(models.IntegerChoices):
        ARCHIVED = 0
        AVAILABLE = 1

    status = models.IntegerField(
        choices=Status.choices,
        default=Status.AVAILABLE
    )

    class Meta:
        abstract = True  # Set this model as Abstract


class Category(BaseModel):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# from shop_projects_app.models import Category
class Creator(BaseModel):
    class Meta:
        verbose_name_plural = "creators"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return f"Creator {self.user}"


class Project(BaseModel):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="projects_for_cats",  # Important  arg!
    )  # Если удалим Category, то Project не дропнится

    # new fields
    creator = models.ForeignKey(
        Creator,
        on_delete=models.PROTECT,
        null=True,
        related_name="projects_for_creators"
    )
    url = models.CharField(max_length=150, null=True)
    other_contributors = models.TextField(null=True)
    # archived = models.BooleanField(default=False)

    # Time fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Product <№{self.id}, {self.name!r}>"


class Donat(BaseModel):
    class Meta:
        verbose_name_plural = "donats"

    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
    )
    projects = models.ManyToManyField(
        Project,
        related_name="donats",
    )
    money = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
