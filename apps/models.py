from django.db import models


class Clients(models.Model):
    name = models.CharField(max_length=65, verbose_name=('name'))
    broker = models.CharField(max_length=65)
    account = models.IntegerField()
    exp_date = models.DateField()

    def __str__(self):
        return self.name


# class Algotrading(models.Model):
#     title = models.CharField(max_length=65)
#     slug = models.SlugField(unique=True)
#     platform = models.CharField(max_length=65)
#     market = models.CharField(max_length=65)
#     account_type = models.CharField(max_length=65)
#     stoploss = models.CharField(max_length=65)
#     gain = models.CharField(max_length=65)
#     volume = models.CharField(max_length=65)
#     time = models.CharField(max_length=65)
#     indicators = models.CharField(max_length=165)
#     timeframe = models.CharField(max_length=65)
#     security = models.CharField(max_length=65)
#     magic = models.CharField(max_length=65)
#     comment = models.CharField(max_length=65)
#     order_type = models.CharField(max_length=65)
#     trailing = models.CharField(max_length=65)
#     goals = models.CharField(max_length=65)
#     functionality = models.CharField(max_length=500)

#     def __str__(self):
#         return self.title
