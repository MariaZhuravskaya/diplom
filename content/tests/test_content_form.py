from content.forms import PublicationForm
from content.models import Publication


class PublicationFormTest:

    def test_request_created(self):
        name = "Интеллект или нет"
        description = "В статье расскажем много интересного об интеллекте"
        paid = True
        price = 1200

        data = {
            "name": name,
            "description": description,
            "paid": paid,
            "price": price
        }

        form = PublicationForm(data=data)
        form.is_valid()
        form.save()
        assert Publication.objects.filter(name=name).count == 1
