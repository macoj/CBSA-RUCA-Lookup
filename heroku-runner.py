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
    
    # catching possible errors. Don't think there should be any, but I don't want
    # to leave the user hanging.
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

    print ">>>>> CBSA CODE", CBSA_code
    print ">>>>> CBSA DESIGNATION", CBSA_designation
    print ">>>>> RUCA CODE", RUCA_code
    #resp = Response(var, status=200, mimetype='text/plain')
    response = '{0}({1})'.format(callback,  {'CBSA_code' : CBSA_code,
                                             'CBSA_designation' : CBSA_designation,
                                             'RUCA_code' : RUCA_code})
    print ">>>> Response", response
    return response

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(environ.get('PORT', 5000))
    # Debugging disabled for production build. 
    app.run(host='0.0.0.0', port=port, debug=False)
