# trashmailapi

Unofficial API for trash/temporary mail services in Python

Currently, only [vsimcard trashmail](https://vsimcard.com/trashmails.php) is supported.

Check the [project wiki](https://codeberg.org/m3r/trashmailapi/wiki) for a more detailed information.

Installation:

`pip install trashmailapi`

Examples:

- Vsimcard:
```
from trashmailapi.vsimcard import Vsimcard

user = Vsimcard("emailaddress")

user.get_emails() # returns email metadata except for body/content

for i in user.inbox:
    if "verify" in i.subject:
        mail = user.get_content(i.id) # returns the email body/content using mail ID's
```
