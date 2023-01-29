# spotify-playlist-generator


## Requirements

1. Token
Head over to <a href = " https://developer.spotify.com/console/get-recommendations/" > Spotify developer console </a>, scroll all the way to the bottom and click on the ‘Get Token’ button.

You need to select the scopes you will use in the endpoint. In this project, the `playlist-modify-public` and the `playlist-modify-private` are required. A documentation regarding scopes is available <a href = 'https://developer.spotify.com/documentation/general/guides/authorization/scopes/'> here </a>


### The console helps you to use the api!!!! And this <a href = "https://developer.spotify.com/documentation/web-api/reference/#/operations/search"> link </a> has the documentation for each endpoint.


2. User id
You can go to <a href = ' https://www.spotify.com/is/account/overview/ '> Spotify account oveview </a> and copy your spotify username.

#### You have to put this info in a .env file, such as the following example

```
TOKEN = "njfhuieafoihfogwuofhwir308748293yr298foq"
USER_ID = "camilabraz03"
```