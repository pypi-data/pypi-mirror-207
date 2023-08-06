from codeoffer import api
from codeoffer import utilities
from codeoffer import exceptions
import base64


class Asset:
    def __init__(self, uuid, identifier, name, description, access, active):
        self.uuid = uuid
        self.identifier = identifier
        self.name = name
        self.description = description
        self.access = access
        self.active = active
        self.session_token = None

    def get_value(self):
        response = api.Controller.sendrequest(api.Request("GET", "https://dev-api.codeoffer.net/v1/app/asset",
                                                          f"uuid={self.uuid}",
                                                          {"OAuth-Session": self.session_token.token}))
        utilities.Utilities.handle_response(response)
        return base64.b64decode(response.data["value"])


class AssetDirectory(list):
    def __init__(self, *args):
        super().__init__(*args)


class App:
    def __init__(self, app_id, session_token):
        self.app_id = app_id
        self.session_token = session_token

    @staticmethod
    def by_session_token(session_token):
        return App(session_token.app, session_token)

    def get_asset_directory(self):
        if self.session_token.account is None:
            raise exceptions.UnauthorizedException("The user most be logged in to perform this action")

        response = api.Controller.sendrequest(api.Request("GET", "https://dev-api.codeoffer.net/v1/app/assets",
                                                          f"uuid={self.app_id}",
                                                          {"OAuth-Session": self.session_token.token}))
        utilities.Utilities.handle_response(response)
        assets = AssetDirectory()
        for item in response.data:
            asset = Asset(item["uuid"], item["identifier"], item["name"], item["description"], item["access"],
                          item["active"])
            asset.session_token = self.session_token
            assets.append(asset)

        return assets
