import viazoom

client = viazoom.ZoomOAuthClient('mw7tNapYSD2iN8zTrBpwTw', 'Tow7uT5XQ0aCvE195oGsjg', '5zFj9zf9qh4VpnYJbtE2R7Q5nVOJbb0w')
access_token = client.get_access_token()
print(access_token)
print(client)

