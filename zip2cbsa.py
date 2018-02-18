# Based on code by:
# John Loeber | Python 2.7.6 | contact@johnloeber.com | Aug 11 2016
from pygeocoder import Geocoder
import pandas as pd


class Zip2CBSA:

    def __init__(self):
        self.df = pd.read_csv("data/ZipToCBSA.csv", dtype="str")

    def zip2cbsa(self, zipcode):
        """
        looks up a zipcode in the spreadsheet, gets the corresponding CBSA code
        and statistical area designation
        """

        row = self.df[self.df.iloc[:,0]==zipcode]
        cbsa_code = row.iloc[0][1]
        cbsa_designation = row.iloc[0][2]
        if pd.isnull(cbsa_code):
            cbsa_code = None
        if pd.isnull(cbsa_designation):
            cbsa_designation = None
        return cbsa_code, cbsa_designation

    def address_to_cbsa(self, address):
        return self.zip2cbsa(Zip2CBSA.zip_lookup(address))

    @staticmethod
    def zip_lookup(address):
        """
        Lookup an address and get the zip code. This is super lazy; it would probably
        be preferable to try to extract the zip from the address string.
        """
        zipcode = Geocoder.geocode(address).postal_code
        return zipcode
