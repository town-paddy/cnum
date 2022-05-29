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

# returns simplified Chinese styled numeral string. 
cnum.scn(123456789.123456789)

# returns traditional Chinese styled numeral string. 
cnum.tcn(123456789.123456789)

# returns Korean styled numeral string. 
cnum.kr(123456789.123456789)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)