from tinydb import TinyDB, Query


class UserService:
    def __init__(self):
        self.db: TinyDB = TinyDB("db.json")
        self.users_table = self.db.table('users')
        self.query: Query = Query()

    def create_user(self, slack_user_id, endpoint=None, api_key=None):
        user_data = {
            'slack_user_id': slack_user_id,
            'endpoint': endpoint,
            'api_key': api_key,
        }
        self.users_table.insert(user_data)
        return user_data

    def get_or_create_user(self, slack_user_id, endpoint=None, api_key=None):
        existing_user = self.users_table.get(
            self.query.slack_user_id == slack_user_id)

        if existing_user:
            return existing_user

        return self.create_user(slack_user_id, endpoint, api_key)

    def update_user(self, slack_user_id, endpoint=None, api_key=None):
        return self.users_table.update(
            {'endpoint': endpoint, 'api_key': api_key},
            self.query.slack_user_id == slack_user_id)
