# CBSA-RUCA-Lookup
Browser application for looking up CBSA and RUCA codes

## CBSA

Maps ZIP-5 codes to CBSA codes. This mapping was obtained from the ``2007 ZIP code to 2006 CBSA`` mapping [published by the census](http://www.census.gov/population/metro/data/other.html).
There is good documentation available on that site. Note that we use a subset of the spreadsheet published there; the iPython Notebook `Make-CBSA-Spreadsheet.ipynb` was used for the conversion.

## RUCA

Maps FIPS 11-digit codes to RUCA secondary codes. The mapping was obtained from the ``2010 Rural Urban Commuter Area Codes`` mapping [published by the USDA](http://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes.aspx).
The dataset downloadable there contains more helpful information. Again we use just a subset of that dataset; the iPython Notebook `Make-RUCA-Spreadsheet.ipynb` was used for the conversion. Note that it reads in a `.csv`, not a `.xlsx` as available on the website. Parsing the Excel File with Pandas leads to problems, so I recommend saving a copy of the Excel File as a `.csv` and then working with that.

Note that there are different types of FIPS-codes, e.g. 15-digit vs. 11-digit. The only difference is that the final four digits of the 15-digit code are [block group and block numbers](http://www.geolytics.com/USCensus,Geocode,Data,Geography,Products.asp). So we can query the [FCC's API](https://www.fcc.gov/general/census-block-conversions-api) for 15-digit FIPS codes and simply truncate the final four. See [here](https://www.policymap.com/blog/2012/08/tips-on-fips-a-quick-guide-to-geographic-place-codes-part-iii/) for another short introduction to FIPS codes.

The FIPS -> RUCA mappings are definitely correct. The Address -> FIPS mappings are subject to greater error. If in doubt, use the mapping tool provided by the government [here](https://geomap.ffiec.gov/FFIECGeocMap/GeocodeMap1.aspx) to double-check your results.

## Structure

The index.html and functions.js are deployed externally, not to Heroku. We query the Heroku server via AJAXin functions.js.

## Use

You can access the tool at johnloeber.com/geolookup.
