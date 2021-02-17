from django.db import models


class Review(models.Model):
    #title_id =  models.ForeignKey(Title,)      # id записи Review
    text = models.CharField(max_length=200)     # текст Review
    score = models.IntegerField()               # Рейтинг
    pub_date = models.DateTimeField(auto_now_add = True)           # дата формирования Review
    author = models.IntegerField(default = 1)  

    #class Meta:
    ##    constraints = [
    #        models.UniqueConstraint(
    #            fields=['text', 'score'],
    #            name='unique_author'
    #        )
    #    ]