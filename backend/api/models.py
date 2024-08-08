from django.db import models


class Player(models.Model):
    player_name = models.CharField(max_length=100)
    player_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.player_name + " " + str(self.player_id)


class Score(models.Model):
    player_name = models.CharField(max_length=100)
    player_id = models.IntegerField()
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    sequence = models.PositiveIntegerField()

    class Meta:
        unique_together = ['player_id', 'sequence']

    def save(self, *args, **kwargs):
        if not self.sequence:
            last_score = Score.objects.filter(player_id=self.player_id).order_by('-sequence').first()
            self.sequence = (last_score.sequence + 1) if last_score else 1
        super().save(*args, **kwargs)
