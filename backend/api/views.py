from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Player, Score
from .serializers import PlayerSerializer, ScoreSerializer
from django.db.models import Max


# View for getting a specific player by ID
@api_view(["GET"])
def player_detail(request, pk):
    player = get_object_or_404(Player, player_id=pk)
    serializer = PlayerSerializer(player)
    return Response(serializer.data)


# View for getting the leaderboard (top scores)
@api_view(["GET"])
def leaderboard(request):
    top_scores = (
        Score.objects.values(
            "player_id", "player_name", "created_at"
        )  # Assuming you have a name field
        .annotate(max_score=Max("score"))
        .order_by("-max_score")
    )

    # Rename fields to be more frontend-friendly
    leaderboard = [
        {
            "player_id": score["player_id"],
            "player_name": score["player_name"],
            "score": score["max_score"],
            "created_at": score["created_at"],
        }
        for score in top_scores
    ]

    return Response(leaderboard)


@api_view(["POST"])
def submit_score(request):
    serializer = ScoreSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
            return Response(serializer.data, status=201)
        except IntegrityError:
            return Response(
                {"error": "Failed to save score. Please try again."}, status=400
            )
    return Response(serializer.errors, status=400)
