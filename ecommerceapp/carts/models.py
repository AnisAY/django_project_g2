from django.db import models
from common.models import Base
from django.contrib.auth import get_user_model
from products.models import Product
from clients.models import Client


class Cart(Base):
    name = models.CharField(max_length=80)
    owner = models.ForeignKey(
        get_user_model(), related_name="carts", on_delete=models.CASCADE
    )
    clients = models.ManyToManyField(Client, related_name='clients')
    products = models.ManyToManyField(Product, related_name="carts")
