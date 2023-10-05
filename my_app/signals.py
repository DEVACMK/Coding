from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Badge, Model3D, UserBadge


@receiver(post_save, sender=Model3D)
def check_badges(sender, instance, **kwargs):
    # Badge "Star"
    if instance.views >= 1000:
        badge, created = Badge.objects.get_or_create(
            name = 'Star',
            description = 'Le modèle a plus de 1k vues',
            critaire = 'views >= 1000'
        )
        if created:
            UserBadge.objects.create(user=instance.user, badge=badge)

    if instance.uploads >= 5:
        badge, created = Badge.objects.get_or_create(
            name = 'Collector',
            description = "L'utilisateur a téléchargé plus de 5 modèles",
            critaire = 'uploads >= 5'
        )
        if created:
            UserBadge.objects.create(user=instance.user, badge=badge)

    if (timezone.now() - instance.user.date_joined).days >= 365:
        badge, created = Badge.objects.get_or_create(
            name = 'Pionneer',
            description = "L'utilisateur est inscrit depuis plus de 1 an sur le site",
            critaire = 'user is registered for more than 1 year'
        )
        if created:
            UserBadge.objects.create(user=instance.user, badge=badge)