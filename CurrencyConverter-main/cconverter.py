import requests

code = input().lower().strip()
actual_currency = requests.get(f"http://www.floatrates.com/daily/{code}.json").json()
if code == 'usd':
    cache = {'eur': actual_currency['eur']['rate']}
elif code == 'eur':
    cache = {'usd': actual_currency['usd']['rate']}
else:
    ex_eur, ex_usd = actual_currency['eur']['rate'], actual_currency['usd']['rate']
    cache = {'usd': ex_usd, 'eur': ex_eur}


while True:
    requested_currency = input().lower().strip()
    if requested_currency == "":
        break

    amount = float(input())

    print("Checking the cache...")
    if requested_currency in cache:
        print("Oh! It is in the cache!")
        print(f"You received {round(amount * cache[f'{requested_currency}'], 2)} {requested_currency.upper()}.")

    else:
        exchange_requested = actual_currency[f'{requested_currency}']['rate']
        print("Sorry, but it is not in the cache!")
        print(f"You received {round(amount * exchange_requested, 2)} {requested_currency.upper()}.")
        cache[f'{requested_currency}'] = exchange_requested
