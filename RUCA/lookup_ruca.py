# John Loeber | Python 2.7.6 | contact@johnloeber.com | Aug 11 2016

"""
Maps an address to a FIPS 11-digit code using the FCC Census Block Conversions
API at https://www.fcc.gov/general/census-block-conversions-api,
then looks the 11-digit code up in the RUCA spreadsheet and returns the RUCA secondary code.
"""

from pygeocoder import Geocoder
import pandas as pd
import requests
import json
user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def address_lookup(address):
    """
    Convert an address to latitude and longitude, then put those into the FCC's API.
    Return the FIPS-11 code.
    """
    latitude, longitude = Geocoder.geocode(address).coordinates
    api_url = "http://data.fcc.gov/api/block/find?latitude={0}&longitude={1}&showall=true&format=json".format(latitude, longitude)
    get = requests.get(api_url, headers = user_agent)
    json_data = json.loads(get.text)
    # now extract the FIPS code from the JSON object, and truncate to 11 digits
    fips_11 = json_data['Block']['FIPS'][:11]
    print "Found FIPS:", fips_11
    return str(fips_11)

def fips_to_ruca(fips):
    """
    Takes a FIPS-11 code, retrieves the matching RUCA secondary code from the
    RUCA spreadsheet.
    """
    # this script assumes it is being run from the top-level directory.
    df = pd.read_csv("RUCA/FIPS-RUCA.csv", dtype="str")
    # first reduce the df to the row with that fips, then extract the RUCA cell value
    return df[df.iloc[:,0]==fips].iloc[0][1]

def address_to_RUCA(address):
    """
    wraps the two above functions.
    """
    return fips_to_ruca(address_lookup(address))
