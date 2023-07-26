from beehiiv.endpoint import Endpoint

class Subscriptions(Endpoint):

    def __init__(self, api_key):
        super().__init__(api_key)

    def create(self, publicationId, email, reactivate_existing=None,
               send_welcome_email=None, utm_source=None, utm_medium=None,
               utm_campaign=None, referring_site=None, referral_code=None,
               custom_fields=[]):
        '''create'''
        return self._make_call(
            "/publications/{}/subscriptions",
            [publicationId],
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

    def index(self, publicationId):
        '''index'''
        return self._make_call(
            "/publications/{}/subscriptions",
            [publicationId],
        ).json()
