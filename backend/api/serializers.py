from rest_framework import serializers
from .models import Player, Score


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ["player_name", "player_id"]

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ["player_name", "score", "created_at","player_id"]
