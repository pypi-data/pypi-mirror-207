from codeoffer import api
from codeoffer import utilities


class User:
    def __init__(self, uuid, username, profile_picture, email, access):
        self.uuid = uuid
        self.username = username
        self.profile_picture = profile_picture
        self.email = email
        self.access = access

    @staticmethod
    def get_user(token):
        response = api.Controller.sendrequest(
            api.Request("GET", "https://dev-api.codeoffer.net/v1/oauth/session/user", headers={"OAuth-Session": token.token}))

        utilities.Utilities.handle_response(response)
        return User(response.data["uuid"], response.data["username"], response.data["profile_picture"],
                    response.data["email"], response.data["access"])
