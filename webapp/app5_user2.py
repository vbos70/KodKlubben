def user2_page(username, foodtype):
    return'''
    <!DOCTYPE=html>
    <html>
      <body>
        <h1>User</h1>
        <p>Hej, {username}, tycker du om {foodtype}?</p>
      </body>
    </html>
    '''.format(username=username, foodtype=foodtype)
