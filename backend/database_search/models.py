from django.db import models

class database_search(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title

# class characters(models.Model):
#     Name = models.TextField()
#     ChapterReveal = models.TextField()
#     EpisodeReveal = models.TextField()
#     YearReveal = models.TextField()
#     Notes = models.TextField()
    
#     def _str_(self):
#         return self.title