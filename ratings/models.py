from django.db import models
from django.contrib.auth.models import User
from exchanges.models import ExchangeRequest


class Rating(models.Model):
    exchange = models.OneToOneField(ExchangeRequest, on_delete=models.CASCADE, related_name='rating')
    rater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='given_ratings')
    rated_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_ratings')
    score = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rater} rated {self.rated_user}: {self.score}/5"
