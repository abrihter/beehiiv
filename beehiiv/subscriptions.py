from beehiiv.endpoint import Endpoint

class Subscriptions(Endpoint):

    def __init__(self, api_key, publicationId):
        super().__init__(api_key)
        self.endpoint = "/publications/{}/subscriptions"
        self.publicationId = publicationId

    def create(self, email, reactivate_existing=None, send_welcome_email=None,
               utm_source=None, utm_medium=None, utm_campaign=None,
               referring_site=None, referral_code=None, custom_fields=[]):
        '''create'''
        return self._make_call(
            [self.publicationId],
            data={
                "email": email,
                "reactivate_existing": reactivate_existing,
                "send_welcome_email": send_welcome_email,
                "utm_source": utm_source,
                "utm_medium": utm_medium,
                "utm_campaign": utm_campaign,
                "referring_site": referring_site,
                "referral_code": referral_code,
                "custom_fields": custom_fields,
            },
            method="POST",
        ).json()

    def index(self):
        '''index'''
        return self._make_call(
            [self.publicationId],
        ).json()

    def show(self, subscriptionId):
        '''show'''
        return self._make_call(
            endpoint=self.endpoint + "/{}"
            [self.publicationId, subscriptionId],
        ).json()

    def update(self, subscriptionId, unsubscribe=None, custom_fields=[]):
        '''update'''
        return self._make_call(
            endpoint=self.endpoint + "/{}"
            [self.publicationId, subscriptionId],
            data={
                "unsubscribe": unsubscribe,
                "custom_fields": custom_fields,
            },
            method="PUT",
        ).json()

    def delete(self, subscriptionId):
        '''delete'''
        return self._make_call(
            endpoint=self.endpoint + "/{}"
            [self.publicationId, subscriptionId],
            method="DELETE",
        ).json()
