import json

from codeoffer import api
from codeoffer import utilities


class SessionToken:
    def __init__(self, token, account, expires, app):
        self.token = token
        self.account = account
        self.expires = expires
        self.app = app

    def wait_for_confirmation(self):
        response = api.Controller.sendrequest(
            api.Request("GET", "https://dev-api.codeoffer.net/v1/oauth/session/state", f"session={self.token}"))
        utilities.Utilities.handle_response(response)
        self.account = response.data["account"]
        return True

    def get_login_link(self):
        return f"http://localhost/oauth/login?session={self.token}"


class SessionTokenOverview:
    def __init__(self, session_token, app, access_token):
        self.session_token = session_token
        self.app = app
        self.access_token = access_token

    class App:
        def __init__(self, uuid, name, icon, vendor):
            self.uuid = uuid
            self.name = name
            self.icon = icon
            self.vendor = vendor

        class Vendor:
            def __init__(self, uuid, username, verified, profile_picture):
                self.uuid = uuid
                self.username = username
                self.verified = verified
                self.profile_picture = profile_picture


def get_session_token(token):
    response = api.Controller.sendrequest(
        api.Request("GET", "https://dev-api.codeoffer.net/v1/oauth/session", f"session={token}&validate=false"))
    utilities.Utilities.handle_response(response)
    vendor = SessionTokenOverview.App.Vendor(response.data["app"]["vendor"]["uuid"],
                                             response.data["app"]["vendor"]["username"],
                                             response.data["app"]["vendor"]["verified"],
                                             response.data["app"]["vendor"]["profile_picture"])
    app = SessionTokenOverview.App(response.data["app"]["uuid"], response.data["app"]["name"],
                                   response.data["app"]["icon"], vendor)
    return SessionTokenOverview(response.data["session_token"], app, response.data["access_token"])


class Session:
    def __init__(self, app_id):
        self.app_id = app_id

    def create_session_token(self):
        response = api.Controller.sendrequest(
            api.Request("PUT", "https://dev-api.codeoffer.net/v1/oauth/session", json.dumps({
                "app": self.app_id
            })))
        utilities.Utilities.handle_response(response)

        return SessionToken(response.data["token"], response.data["account"], response.data["expires"],
                            response.data["app"])
