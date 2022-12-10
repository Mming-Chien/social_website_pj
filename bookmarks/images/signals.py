from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Image
@receiver(m2m_changed, sender=Image.users_like.through)
def users_like_changed(sender, instance, **kwargs):
	''' Change total_likes according to users_like changes'''
	instance.total_likes = instance.users_like.count()
	instance.save()