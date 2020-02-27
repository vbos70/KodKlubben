def user_page(username):
    return'''
    <!DOCTYPE=html>
    <html>
      <head>
        <link rel="stylesheet" type="text/css" href="/static/style.css">
      </head>
      <body>
        <h1>App5 user</h1>
        <p>Hej, {username}, tycker du om kex?</p>
      </body>
    </html>
    '''.format(username=username)
