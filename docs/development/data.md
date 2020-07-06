# Internal Data

Various data is contained internally in the `_data` folder. If file names are
changed ensure the `MANIFEST.in` is updated.

### Libor Rates
The libor rates for 1 month USD can be updated by downloading the CSV data
from https://fred.stlouisfed.org/series/USD1MTD156N

Ensure you select `Max` for the time window.

### Short Term Interest Rates
The interbank short term interest rates can be updated by downloading the CSV
data at https://data.oecd.org/interest/short-term-interest-rates.htm

### Economic Events
The economic events can be updated from downloading the CSV data from MyFXBook
https://www.myfxbook.com/forex-economic-calendar

Note that a maximum 3 month range can be filtered and so yearly quarters must be
downloaded manually and stitched together into a single CSV. The script for
this will be added to the repository soon.