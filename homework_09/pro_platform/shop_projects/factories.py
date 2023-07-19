from django.contrib.auth.models import User
from django.core.management import BaseCommand

import factory
from django.db.models.signals import post_save
from django.utils import timezone
from factory.django import DjangoModelFactory

from shop_projects.models import Category, Project, Creator, OrderPaymentDetails, Order


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category
        django_get_or_create = ("name",)

    name = factory.Faker("word")
    description = factory.Faker('sentence', nb_words=15)
    status = Category.Status.AVAILABLE


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("username",)

    username = factory.Faker('word')
    password = factory.Faker('password')


class CreatorFactory(DjangoModelFactory):
    class Meta:
        model = Creator
        django_get_or_create = ("user",)

    user = factory.SubFactory(UserFactory)
    rating = factory.Faker('pyint', min_value=0, max_value=5)
    status = True


# create new user, creator and project
class ProjectFactoryWithSubFactory(DjangoModelFactory):
    class Meta:
        model = Project

    name = factory.Faker("sentence", nb_words=3)
    price = factory.Faker('pydecimal', min_value=0, max_value=1000)
    description = factory.LazyAttribute(lambda o: f'{o.name} service')
    category = factory.SubFactory(CategoryFactory)  # with creating new category
    creator = factory.SubFactory(CreatorFactory)  # with creating new creator
    # creator = factory.LazyFunction(choice([i.user.id for i in Creator.objects.all()]))  # doesnt work
    status = factory.Iterator(Project.Status.values)


# create ONLY new project (user, creator from db)
class ProjectFactoryBasedDB(DjangoModelFactory, ):
    class Meta:
        model = Project

    name = factory.Faker("sentence", nb_words=3)
    price = factory.Faker('pydecimal', min_value=0, max_value=1000)
    description = factory.LazyAttribute(lambda o: f'{o.name} service')
    # important!!! number of category should be equal creator (zip analogy)
    category = factory.Iterator([i for i in Category.objects.all()])  # with category from db
    print(Category.objects.all())
    creator = factory.Iterator([i for i in Creator.objects.all()])  # with creator from db
    print(Creator.objects.all())
    status = factory.Iterator(Project.Status.values)

    # @classmethod
    # def create_batch_custom(cls, size, **kwargs):
    #     cls.category = factory.Iterator([i for i in kwargs["category"]])
    #     cls.creator = factory.Iterator([i for i in kwargs["creator"]])
    #
    #     return super().create_batch(size)

#
# class OrderPaymentDetailsFactory(DjangoModelFactory):
#     class Meta:
#         model = OrderPaymentDetails
#
#
# @factory.django.mute_signals(post_save)
# class OrderFactory(DjangoModelFactory):
#     class Meta:
#         model = Order
#
#     user = factory.Iterator(User.objects.all())
#     # products = factory.Iterator(Product.objects.all())
#     promocode = factory.Faker("word")
#     # due to RelatedFactory OrderPaymentDetails will create ONLY AFTER Order creation
#     payment_details = factory.RelatedFactory(
#         OrderPaymentDetailsFactory,
#         factory_related_name="order",
#         # payed_at=factory.LazyFunction(datetime.utcnow)
#         payed_at=factory.LazyFunction(timezone.now)
#     )
#
#     # ManyToManyField
#     @factory.post_generation
#     def projects(self, create, extracted, **kwargs):
#         if not create:
#             # Simple build, do nothing.
#             return
#
#         if extracted:
#             # A list of groups were passed in, use them
#             for project in extracted:
#                 self.projects.add(project)
#
#     # branches of creation by flags (Trait name = True)
#     class Params:
#         empty_promocode = factory.Trait(
#             promocode="",
#             payment_details=None,
#         )
#         paid = factory.Trait(
#             payment_details__card_ends_with=factory.Faker("word"),
#             payment_details__payed_at=factory.LazyFunction(timezone.now),
#         )
#         paid_confirmed = factory.Trait(
#             payment_details__card_ends_with=factory.Faker("word"),
#             payment_details__status=OrderPaymentDetails.Status.CONFIRMED,
#             payment_details__payed_at=factory.LazyFunction(timezone.now),
#         )


