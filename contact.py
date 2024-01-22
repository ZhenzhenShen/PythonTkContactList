class Contact:
    def __init__(self, name, company, phone, email):
        self.name = name
        self.company = company
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Company: {self.company}, Phone: {self.phone}, Email: {self.email}"