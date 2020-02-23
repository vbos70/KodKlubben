def doctype(v="html"):
    return "<!DOCTYPE {v}>".format(v=v)

def html(txt):
    return '''
    <html>
        {txt}
    </html>
    '''.format(txt=txt)

def body(txt):
    return '''
    <body>
        {txt}
    </body>
    '''.format(txt=txt)

def h1(txt):
    return '''
    <h1>
        {txt}
    </h1>'''.format(txt=txt)

def p(txt):
    return '''
    <p>
       {txt}
   </p>
    '''.format(txt=txt)

                    
