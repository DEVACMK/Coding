from django.db import models
from django.contrib.auth.models import User


class Model3D(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='model_image/')
    views = models.IntegerField(default=0)
    uploads = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # super().save(*args, **kwargs)
        if not self.id:
            # Si l'objet est nouveau (pas encore enregistré), appelez increment_views_and_uploads
            self.views += 1
            self.uploads += 1
        super(Model3D, self).save(*args, **kwargs)

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Model3D'
        verbose_name_plural = 'Model3Ds'

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return f"{self.user}"


class Badge(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    critaire = models.CharField(max_length=255)

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Badge'
        verbose_name_plural = 'Badges'

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return f"{self.name}"
    

class UserBadge(models.Model):
    """Model definition for MODELNAME."""

    # TODO: Define fields here
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    date_awarded = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'UserBadge'
        verbose_name_plural = 'UserBadges'

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return f"{self.user} -> {self.badge}"
