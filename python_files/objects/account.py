class Account:

    def __init__(self, username, bio, email, phone):
        self.ID = 0
        self.username = username
        self.bio = bio
        self.email = email
        self.phone = phone

    def __set_id__(self, ID):
        self.ID = ID
