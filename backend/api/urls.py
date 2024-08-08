from django.urls import path
from .views import player_detail, leaderboard, submit_score

urlpatterns = [
    path("player/<int:pk>/", player_detail, name="player-detail"),
    path("leaderboard", leaderboard, name="leaderboard"),
    path("submit_score", submit_score, name="submit-score"),
]
