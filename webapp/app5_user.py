def user_page(username):
    return'''
    <!DOCTYPE=html>
    <html>
      <body>
        <h1>User</h1>
        <p>Hej, {username}, tycker du om kex?</p>
      </body>
    </html>
    '''.format(username=username)
