from django.db import models
from common.models import Base
from django.contrib.auth import get_user_model


class Client(Base):
    name = models.CharField(max_length=80)
    prenom = models.CharField(max_length=80)
