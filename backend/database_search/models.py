from django.db import models

# class database_search(models.Model):
#     title = models.CharField(max_length=120)
#     description = models.TextField()
#     completed = models.BooleanField(default=False)

#     def _str_(self):
#         return self.title

class characters(models.Model):
    name = models.TextField(null = True, blank = True)
    chapter_reveal = models.TextField(null = True, blank = True)
    episode_reveal = models.TextField(null = True, blank = True)
    year_reveal = models.TextField(null = True, blank = True)
    notes = models.TextField(null = True, blank = True)
    
    def _str_(self):
        return self.name