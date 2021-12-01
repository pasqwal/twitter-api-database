from datetime import datetime

class Tweet:
    #def __init__(self, text, created_at=datetime.now().strftime("%d/%m/%Y %H:%M:%S")):
    def __init__(self, text, created_at=datetime.now()):
        self.id = None
        self.text = text
        self.created_at = created_at
        self.updated_at = None

    def updated(self):
        self.updated_at = datetime.now()
