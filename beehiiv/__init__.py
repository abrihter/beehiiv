from beehiiv.subscriptions import Subscriptions

class BeeHiiv:

    def __init__(self, api_key):
        '''init'''
        self.subscriptions = Subscriptions(api_key)
