# John Loeber | contact@johnloeber.com | August 2016 | contact@johnloeber.com

from CBSA import lookup_cbsa
from RUCA import lookup_ruca
from flask import Flask, request
from os import environ

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    print ">>>> Got a request..."
    print ">>>> Request args", request.args
    callback = request.args.get('callback')
    address  = request.args.get('address')
    
    # catching errors in case of malformed input.
    try:
        CBSA_code, CBSA_designation = lookup_cbsa.address_to_CBSA(address)
    except:
        print "Error was generated!"
        CBSA_code, CBSA_designation = "ERROR", "ERROR"
    try:
        RUCA_code = lookup_ruca.address_to_RUCA(address)
    except:
        print "Error was generated!"
        RUCA_code = "ERROR"

    # there's no need to return the five-digit CBSA code as well.
    response = '{0}({1})'.format(callback,  {'CBSA_designation' : CBSA_designation,
                                             'RUCA_code' : RUCA_code})
    print ">>>> Response", response
    return response

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(environ.get('PORT', 5000))
    # Debugging disabled for production build. 
    app.run(host='0.0.0.0', port=port, debug=False)
