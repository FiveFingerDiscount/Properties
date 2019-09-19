# Properties

## Usage

```bash
scrapy crawl manual -s CLOSESPIDER_ITEMCOUNT=30 -t csv -o items.csv
```

Where `CLOSESPIDER_ITEMCOUNT` is the number of maximum items to be crawled.

Note: the output is appended to the `items.csv` file. Using `-o - > items.csv` also includes all `print(...)` statements fromt he code.
