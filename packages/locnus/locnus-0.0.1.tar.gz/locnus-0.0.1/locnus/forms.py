from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import CharField, Form, ModelForm, PasswordInput
from mastodon import MastodonIllegalArgumentError

from .models import Account, Server


class ServerForm(ModelForm):
    class Meta:
        model = Server
        fields = ["api_base_url"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Submit"))


class AccountForm(ModelForm):
    password = CharField(widget=PasswordInput())

    class Meta:
        model = Account
        fields = ["server", "username"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Submit"))

    def full_clean(self):
        super().full_clean()
        try:
            self.instance.access_token = self.instance.server.get_access_token(
                self.cleaned_data["username"], self.cleaned_data["password"]
            )
        except MastodonIllegalArgumentError:
            self.add_error("password", "Invalid username or password")


class TootForm(Form):
    content = CharField()

    class Meta:
        fields = ["content"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Submit"))
