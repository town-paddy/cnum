import cnum

def usd2jpy(usd):
    return usd * 127.13

def usd2rmd(usd):
    return usd * 6.74

def usd2hkd(usd):
    return usd * 7.86

def usd2krw(usd):
    return usd * 0.11

if __name__ == '__main__':
    APPLE_MARKET_VALUE = 2421953134592
    print("=== Apple company's market value in 2022 ===")
    print('- JPY: %s' % cnum.jp(usd2jpy(APPLE_MARKET_VALUE)))
    print('- RMD: %s' % cnum.scn(usd2rmd(APPLE_MARKET_VALUE)))
    print('- HKD: %s' % cnum.tcn(usd2hkd(APPLE_MARKET_VALUE)))
    print('- KRW: %s' % cnum.kn(usd2krw(APPLE_MARKET_VALUE)))
