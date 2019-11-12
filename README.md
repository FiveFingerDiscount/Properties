# Properties

## Usage

```bash
scrapy crawl huizenzoeker -s CLOSESPIDER_ITEMCOUNT=30 -t csv -o items.csv
```

Where `CLOSESPIDER_ITEMCOUNT` is the number of maximum items to be crawled.

Note: the output is appended to the `items.csv` file. Using `-o - > items.csv` also includes all `print(...)` statements fromt he code.

'Geolocator.py' can be used to add the geolocation of the crawled address to the 'items.csv'