# John Loeber | contact@johnloeber.com | August 2016 | contact@johnloeber.com

from flask import Flask, request, redirect
from os import environ
# only import stdout if you need to debug. Then use stdout.flush() after print.
# from sys import stdout

"""
This script runs on Heroku, and is connected to Twilio such that it handles
incomingo messages, responding in turn with appropriate statistics for the
poker hand described in the message. It determines the statistics by parsing
the described hand, and looking it up in one of the lookup-tables in this
directory.
"""

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    print "Got a request..."
    return "Hello World!"    

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(environ.get('PORT', 5000))
    # Debugging disabled for production build. 
    app.run(host='0.0.0.0', port=port, debug=False)
