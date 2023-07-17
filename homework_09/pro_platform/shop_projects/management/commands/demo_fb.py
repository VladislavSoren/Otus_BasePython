from random import choice

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
    description = factory.Faker('sentence', nb_words=30)
    status = True


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


class ProjectFactory(DjangoModelFactory):
    class Meta:
        model = Project

    name = factory.Faker("sentence", nb_words=3)
    price = factory.Faker('pydecimal', min_value=0, max_value=1000)
    # description = factory.Faker('sentence', nb_words=30)
    description = factory.LazyAttribute(lambda o: f'{o.name} service')
    # category = factory.SubFactory(CategoryFactory)  # with creating new category
    category = factory.Iterator([i for i in Category.objects.all()])  # with created category
    # creator = factory.SubFactory(CreatorFactory)
    creator = factory.Iterator([i for i in Creator.objects.all()])  # work
    # creator = factory.LazyFunction(choice([i.user.id for i in Creator.objects.all()]))  # try random choice
    status = factory.Iterator(Project.Status.values)


class OrderPaymentDetailsFactory(DjangoModelFactory):
    class Meta:
        model = OrderPaymentDetails


@factory.django.mute_signals(post_save)
class OrderFactory(DjangoModelFactory):
    class Meta:
        model = Order

    user = factory.Iterator(User.objects.all())
    # products = factory.Iterator(Product.objects.all())
    promocode = factory.Faker("word")
    payment_details = factory.RelatedFactory(
        OrderPaymentDetailsFactory,
        factory_related_name="order",
        # payed_at=factory.LazyFunction(datetime.utcnow)
        payed_at=factory.LazyFunction(timezone.now)
    )

    @factory.post_generation
    def products(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for product in extracted:
                self.products.add(product)

    # branches of creation by flags (Trait name = True)
    class Params:
        empty_promocode = factory.Trait(
            promocode="",
            payment_details=None,
        )
        paid = factory.Trait(
            payment_details__card_ends_with=factory.Faker("word"),
            payment_details__payed_at=factory.LazyFunction(timezone.now),
        )
        paid_confirmed = factory.Trait(
            payment_details__card_ends_with=factory.Faker("word"),
            payment_details__status=OrderPaymentDetails.Status.CONFIRMED,
            payment_details__payed_at=factory.LazyFunction(timezone.now),
        )


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Start factory boy")

        # category = CategoryFactory()
        # print(category)

        # category = CategoryFactory(status=False)
        # print(category)

        # project = ProjectFactory()
        # print(project)
        # print(project.category)
        # print(project.creator)
        #
        # project = ProjectFactory()
        # print(project)
        # print(project.category)
        # print(project.creator)

        # projects = ProjectFactory.create_batch(2)

        # order = OrderFactory.build(empty_promocode=True)
        order = OrderFactory.build(paid=True)
        print(order, [order.promocode, order.payment_details.card_ends_with])
