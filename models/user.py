from utils.Exceptions import validation_error, authentication_error, inactive_account_error
from utils.validators import validate_password
from services.wallet import Wallet


class User:
    role = "user"

    def __init__(self, name, username, password, email, is_active=True, user_id=None):
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.is_active = is_active
        self.user_id = user_id

    def check_password(self, password):
        if self.password != password:
            raise authentication_error()
        return True

    def authenticate(self, password):
        self.check_password(password)
        if not self.is_active:
            raise inactive_account_error()
        return True

    @classmethod
    def login(cls, users, username, password):
        for user in users:
            if user.username == username:
                user.authenticate(password)
                return user
        raise authentication_error()

    def change_password(self, new_password):
        if not isinstance(new_password, str) or not validate_password(new_password):
            raise validation_error()
        self.password = new_password

    def information(self):
        return {
            "role": self.role,
            "name": self.name,
            "username": self.username,
            "password": "******",
            "email": self.email,
            "is_active": self.is_active,
        }


class Manager(User):
    role = "manager"

    def __init__(self, name, username, password, email, is_active=True, user_id=None):
        super().__init__(name, username, password, email, is_active, user_id)

    def manage_users(self):
        pass

    def manage_venues(self):
        pass

    def manage_courses(self):
        pass

    def manage_subscription(self):
        pass

    def get_report(self):
        pass


class Trainer(User):
    role = "trainer"

    def __init__(self, name, username, password, email, is_active=True, user_id=None):
        super().__init__(name, username, password, email, is_active, user_id)

    def view_my_classes(self):
        pass

    def set_workout_plan(self):
        pass


class Member(User):
    role = "member"

    def __init__(self, name, username, password, email, is_active=True, user_id=None):
        super().__init__(name, username, password, email, is_active, user_id)
        self.wallet = Wallet(user_id, username)
        self.subscription = None

    @property
    def subscription_status(self):
        if self.subscription is None:
            return "No subscription"
        return self.subscription.status