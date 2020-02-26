from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User

# Create your models here.
class Action(models.Model):
    user = models.ForeignKey(
        User, 
        db_index=True, 
        related_name='actions',
        on_delete=models.CASCADE
    )
    verb = models.CharField(max_length=255)
    created = models.DateTimeField(db_index=True, auto_now_add=True)
    target_ct = models.ForeignKey(
        ContentType, 
        blank=True,
        null=True,
        related_name='target_obj',
        on_delete=models.CASCADE
    )
    target_id = models.PositiveIntegerField(
        null=True,
        blank=True,
        db_index=True
    )
    target = GenericForeignKey('target_ct', 'target_id')

    
    class Meta:
        ordering = ('-created',)