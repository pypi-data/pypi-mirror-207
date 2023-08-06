# CodeOffer Python Package

CodeOffer is a Python package that provides an API wrapper for the public CodeOffer API. The package simplifies authentication and management of in-app assets for developers who use the CodeOffer API in their applications.

## Installation

To install the package, run the following command:

```py
pip install codeoffer
``` 

## Usage

Import the `codeoffer` class from the package:

### Authentication & Sessions

Initialize a new session, but first you need to import the `oauth` class from `codeoffer`

```py
from codeoffer import oauth
```

After that you can create a new session token:

```py
token = session.create_session_token()
```

Now get the login link and ask the user to log in:
`token.get_login_link()`

Right after that call the `token.wait_for_confirmation()` method, this method will wait until the user completed the login-process.

To return the current logged in user you need to import the `user` class from `codeoffer`

```py
from codeoffer import user
```

Then you can return the current user by using the `get_user` method and passing the token as a parameter:

```py
user = user.User.get_user(token)
```

And now you can get the username, email, profile picture and access to the current logged in app (if the user purchased / downloaded the app with his account)

```py
print(f"Hey {user.username}")
```

### Assets

You can return all the apps your app contains.

First import the `app` class from `codeoffer`

```py
from codeoffer import app
```

Then you need to initialize the app with a session token.

```py
app = app.App.by_session_token(token)
```

After that you can return all the assets your app contains and return properties like the name, identifier and if the user has access to that asset.

```py
assets = app.get_asset_directory()
```
```py
for asset in assets:  
	print(f"{asset.name}: {asset.access}")
```

#### Complete Example
```py
from codeoffer import oauth  
from codeoffer import app  
from codeoffer import user  
      
session = oauth.Session("10aa641e562bdd82d2f8449d")  
token = session.create_session_token()  
token.get_login_link()  
token.wait_for_confirmation()  
user = user.User.get_user(token)  
print(f"Hey {user.username}")  
app = app.App.by_session_token(token)  
assets = app.get_asset_directory()  
for asset in assets:  
	print(f"{asset.name}: {asset.access}")
```

## License

This package is licensed under the MIT License.