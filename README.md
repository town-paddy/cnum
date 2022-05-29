# cnum

cnum is a Python library for changing int and float value to Chinese numeral format string.

Chinese numeral format is adopted following languages:
- Japanese
- Simplified Chinese
- Traditional Chinese 
- Korean

For each languages 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install cnum
```

## Usage

```python
import cnum

# returns Japanese styled numeral string.
cnum.jp(123456789.123456789)
'1億2345万6789 1分2厘3毛4糸5忽'

# returns simplified Chinese styled numeral string. 
cnum.scn(123456789.12345)
'1亿2345万6789 1分2厘3毫4丝5忽'

# returns traditional Chinese styled numeral string. 
cnum.tcn(123456789.12345)
'1億2345萬6789 1分2厘3毫4絲5忽'

# returns Korean styled numeral string. 
cnum.kr(123456789.12345)
'1억2345만6789 1分2厘3毛4糸5忽'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)