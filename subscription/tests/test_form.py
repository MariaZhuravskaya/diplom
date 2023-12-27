from content.models import Publication
from subscription.forms import SubscriptionForm
from subscription.models import Subscription


class SubscriptionFormTest:

    def test_request_created(self):
        publication = Publication.objects.create(name='Big', description='Bob', price=12000, is_publication=True)
        is_active = True

        data = {
            "publication": publication,
            "is_active": is_active,
        }

        form = SubscriptionForm(data=data)
        form.is_valid()
        form.save()
        assert Subscription.objects.filter(publication=publication).count == 1
