from django.db.models import Sum
from .models import Entity

num1 = Entity.objects.filter(buy_currency="cny").aggregate(Sum('buy_amount'))
num1['buy_amount__sum']
num2 = Entity.objects.filter(sell_currency="cny").aggregate(Sum('sell_amount'))
num2['sell_amount__sum']
count = Entity.objects.count()

# http://stackoverflow.com/a/6481297/1240067