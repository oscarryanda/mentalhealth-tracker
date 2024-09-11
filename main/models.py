from django.db import models
import uuid

class MoodEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mood = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    feelings = models.TextField()
    mood_intensity = models.IntegerField()

    class Meta:
        app_label = 'main'

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5
