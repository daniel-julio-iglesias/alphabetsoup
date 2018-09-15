#!/usr/bin/env python
# -*- coding: utf-8 -*-


# /usr/bin/env python3
#  -*- coding: ascii -*-

#   coding: cp1252
# Any of the following string literal forms work in latin-1.
# Changing the encoding above to either ascii or utf-8 fails,
# because the 0xc4 and 0xe8 in myStr1 are not valid in either.



# Main application module

# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
# microblog/
#   venv/
#   app/
#    __init__.py
#    routes.py
#  microblog.py

# Linux
# export FLASK_APP=alphabetsoup.py
# MS Windows
# set FLASK_APP=alphabetsoup.py

# flask run
# python alphabetsoup.py

# http://localhost:5000/
# http://localhost:5000/index

from app import app, db
from app.models import User


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}


if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True, threaded=False)
