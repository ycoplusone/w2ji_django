from django.test import TestCase
from .models import c, q
from django.utils import timezone

q.objects.all()

a = q(q_t="What's new?ffffff", p_d=timezone.now())
a.save()
print( a.id )
