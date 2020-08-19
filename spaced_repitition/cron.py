from . models import Card


def decrement_days_till_study():
    for card in Card.objects.all():
        if int(card.days_till_study) > 1:
            card.days_till_study -= 1
            card.save()

    # - FInd way to change one
    # This is how we did it ::::
    # x = Card.objects.all()
    # card_1 = x[0]
    # >>> card_1.days_till_study
    # >>> card_1.days_till_study = 5
    # >>> card_1.save()
    # 1 Find way to change all values of days_till_study
    # all_models = Card.objects.all()
    # all_models.update(days_till_study=50)

    # 1. Get all objects
    # 2. Decrement days_till_study
    # for card in Cards:
    #     if days_till_study > 1:
    #         days_till_study -= 1
    #         card.save()

    # Note this is the old one.
 # def decrement_days_till_study(self):
 #        for card in Cards:
 #            x = str(datetime.now())
 #            if x[11:] == '21:33:00.000000':
 #                if days_till_study > 1:
 #                    days_till_study -= 1
 #                    card.save()

    # if days_till_study > 1:
    #     x = str(datetime.now())
    #     if x[11:] == '13:08:00.000000':
    #         days_till_study -= 1
