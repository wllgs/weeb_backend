from rest_framework import serializers
from .models import Article, ContactMessage
from .ml import satisfaction_score, is_satisfied

class ArticleSerializer(serializers.ModelSerializer):
    """Sérialiseur CRUD pour les articles."""
    class Meta:
        model = Article
        fields = ["id", "title", "content", "is_published", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Le titre doit faire au moins 3 caractères.")
        return value


class ContactMessageSerializer(serializers.ModelSerializer):
    """
    Sérialiseur de création d'un message de contact.
    La satisfaction est calculée côté serveur à partir du `message`.
    """
    class Meta:
        model = ContactMessage
        fields = ["id", "name", "email", "message", "satisfaction", "satisfaction_score", "created_at"]
        read_only_fields = ["id", "satisfaction", "satisfaction_score", "created_at"]

    def create(self, validated_data):
        msg = validated_data.get("message", "")
        score = satisfaction_score(msg)
        validated_data["satisfaction_score"] = score
        validated_data["satisfaction"] = is_satisfied(msg)
        return super().create(validated_data)

