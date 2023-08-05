import requests as req
from bs4 import BeautifulSoup as bs
import re
import time

TRASHMAIL:str = "https://vsimcard.com/trashmails.php?search="
TRASHCONTENT:str = "https://vsimcard.com/mail.php?search="

class MailObject:
    def __init__(self, username: str, subject: str, sender: str, id: int, timestamp:str):
        self.username = username
        self.subject = subject
        self.sender = sender
        self.id = id
        self.timestamp = timestamp
        self.content = None
    
    def __repr__(self):
        return str({"username": self.username, "subject" : self.subject, "sender" : self.sender, "timestamp" : self.timestamp, "content": self.content, "id" : self.id})

class Vsimcard:
    def __init__(self, addy:str):
        self.addy = addy
        self.inbox = []
        self.contentbox = []

    def get_emails(self):
        returned = req.get(TRASHMAIL + self.addy)
        returned.raise_for_status()
        inboxhtml = returned.text
        if f"Keine E-Mails für <b>{self.addy}@vsimcard.com</b>" in inboxhtml:
            return self.inbox
        soup = bs(inboxhtml, 'html.parser')
        emails = soup.find_all('div', {'class': 'email'})

        for email in emails:
            mailid = email.find('iframe').get('name')[5:]
            sender = email.find_all('td', {'bgcolor': '#FFFFFF'})[2].text.strip()
            if "@" not in sender:
                tdtag = email.find_all('td', {'bgcolor': '#FFFFFF'})[2].findChildren()
                sender = re.findall(r"[\w\.-]+@[\w\.-]+", str(*tdtag))[0]
            subject = email.find('b').text
            timestamp = email.find_all('td', {'bgcolor': '#FFFFFF'})[3].text.strip()

            mailobj = MailObject(self.addy, subject, sender, mailid, timestamp)

            self.inbox.append(mailobj)
        return self.inbox

    def get_content(self, mailid):
        for mail in self.inbox:
            if mail.content and mail.id == mailid:
                return mail.content
            elif not mail.content and mail.id == mailid:
                retrievedcontent = req.get(f"{TRASHCONTENT}{self.addy}&nr={mailid}").text
                mail.content = retrievedcontent
                self.contentbox.append(mail.content)
                return mail.content
