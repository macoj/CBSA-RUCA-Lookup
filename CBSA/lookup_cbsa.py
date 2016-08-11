# John Loeber | Python 2.7.6 | contact@johnloeber.com | Aug 11 2016

from pygeocoder import Geocoder
import pandas as pd

def zip_lookup(address):
    """
    Lookup an address and get the zip code. This is super lazy; it would probably
    be preferable to try to extract the zip from the address string.
    """
    zipcode = Geocoder.geocode(address).postal_code
    return zipcode
  
def zip_to_CBSA(zipcode):
    """
    looks up a zipcode in the spreadsheet, gets the corresponding CBSA code
    and statistical area designation
    """
    df = pd.read_csv("ZipToCBSA.csv", dtype="str")
    row = df[df.iloc[:,0]==zipcode]
    CBSA_code = row.iloc[0][1]
    CBSA_designation = row.iloc[0][2]
    return CBSA_code, CBSA_designation

def address_to_CBSA(address):
    """
    wrapper for the two functions above.
    """
    return zip_to_CBSA(zip_lookup(address))
