# U.S. Zip Code to Core-Based Satistical Area (CBSA)

Usage as simple as:

```python
import zip2cbsa
converter = zip2cbsa.Zip2CBSA()
cbsa, designation = converter.zip2cbsa(['32901'])
print cbsa, designation
```
results
```
37340 Metropolitan Statistical Area
```

It also works with lists:
```python
zipcodes = [32901, 10033, 90003]
converter.zip2cbsa(zipcodes)
```
results
```
array([['37340', 'Metropolitan Statistical Area'],
       ['35620', 'Metropolitan Statistical Area'],
       ['31100', 'Metropolitan Statistical Area']], dtype=object)
```


This code is based on https://github.com/Datamine/CBSA-RUCA-Lookup. 
