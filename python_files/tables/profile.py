def __blueprint__():
    return f'''
        code VARCHAR UNIQUE, 
        name VARCHAR, 
        bio VARCHAR, 
        email VARCHAR, 
        phone VARCHAR
        '''


def __keys__():
    return "code, name, bio, email, phone"


class Profile:

    def __init__(self, code, name, bio, email, phone):
        self.code = code
        self.name = name
        self.bio = bio
        self.email = email
        self.phone = phone

    def __values__(self):
        return self.code, self.name, self.bio, self.email, self.phone

    def __repr__(self):
        return f'<Profile> {self.name}'
