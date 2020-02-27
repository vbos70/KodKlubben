def user2_page(username, foodtype):
    return'''
    <!DOCTYPE=html>
    <html>
      <head>
        <link rel="stylesheet" type="text/css" href="/static/style.css">
      </head>
      <body>
        <h1>App5 Tycker du om?</h1>
        <p>Hej, {username}, tycker du om {foodtype}?</p>
      </body>
    </html>
    '''.format(username=username, foodtype=foodtype)
