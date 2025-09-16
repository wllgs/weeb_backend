from django.db import models

class Article(models.Model):
    """Article de blog basique pour Weeb."""
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    """Message de contact + évaluation de satisfaction (0 ou 1)."""
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    satisfaction = models.BooleanField(
        help_text="1 si satisfait, 0 sinon", default=False
    )
    satisfaction_score = models.FloatField(
        help_text="Score brut utilisé par le classifieur (0..1).", default=0.0
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} <{self.email}>"

