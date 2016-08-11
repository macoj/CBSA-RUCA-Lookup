# CBSA-RUCA-Lookup
Browser application for looking up CBSA and RUCA codes

## CBSA

Maps ZIP-5 codes to CBSA codes. This mapping was obtained from the ``2007 ZIP code to 2006 CBSA`` mapping [published by the census](http://www.census.gov/population/metro/data/other.html).
There is good documentation available on that site. Note that we use a subset of the spreadsheet published there; the iPython Notebook `Make-CBSA-Spreadsheet.ipynb` was used for the conversion.

## RUCA

Maps FIPS 11-digit codes to RUCA secondary codes. The mapping was obtained from the ``2010 Rural Urban Commuter Area Codes`` mapping [published by the USDA](http://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes.aspx).
The dataset downloadable there contains more helpful information. Again we use just a subset of that dataset; the iPython Notebook `Make-RUCA-Spreadsheet.ipynb` was used for the conversion. See [here](https://www.policymap.com/blog/2012/08/tips-on-fips-a-quick-guide-to-geographic-place-codes-part-iii/) for a short introduction to FIPS codes.


