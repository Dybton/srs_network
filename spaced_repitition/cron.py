from . models import Card


def decrement_days_till_study():
    for card in Card.objects.all():
        if int(card.days_till_study) > 1:
            card.days_till_study -= 1
            card.save()
