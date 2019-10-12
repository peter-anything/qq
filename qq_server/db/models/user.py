class User(object):
    id = 0
    qq_id = 0
    nickname = ''
    username = ''
    mobile = ''
    password = ''
    email = ''
    avatar = ''
    address = ''
    sex = 0
    age = 0
    created_at = None
    updated_at = None

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.qq_id = kwargs.get('qq_id')
        self.nickname = kwargs.get('nickname')
        self.username = kwargs.get('username')
        self.mobile = kwargs.get('mobile')
        self.password = kwargs.get('password')
        self.email = kwargs.get('email')
        self.avatar = kwargs.get('avatar')
        self.address = kwargs.get('address')
        self.sex = kwargs.get('sex')
        self.age = kwargs.get('age')
        self.created_at = kwargs.get('created_at')
        self.updated_at = kwargs.get('updated_at')

    @property
    def attributes(self):
        return self.__dict__

    @property
    def serialized_obj(self):
        attributes = self.attributes
        attributes.pop('created_at')
        attributes.pop('updated_at')
        return attributes
