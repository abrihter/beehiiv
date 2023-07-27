# beehiiv
Python wrapper for BeeHiiv API

#### Install
```
pip3 install beehiiv
```

### Example
```Python
import os
import beehiiv

PUBLICATION_ID = os.environ['BEEHIIV_PUBLICATION_ID']
API_KEY = os.environ['BEEHIIV_API_KEY']

bh = beehiiv.BeeHiiv(api_key=API_KEY, publicationId=PUBLICATION_ID)
subscriptions = bh.subscriptions.index(
  expand=["stats", "custom_fields"],
  limit=5
)
print(subscriptions)
```
