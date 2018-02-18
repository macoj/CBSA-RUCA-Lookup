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
        if type(zipcode) is not list:
            zipcode = [zipcode]
        zipcode = map(str, zipcode)
        df_slice = self.df[self.df.ZIP5.isin(zipcode)]
        result = df_slice.set_index('ZIP5').loc[zipcode].values
        result = result if len(result) > 1 else result[0]
        return result

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
