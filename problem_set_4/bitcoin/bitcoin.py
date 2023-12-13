import requests
import sys

# Check cmd line argument
if len(sys.argv) != 2:
    sys.exit("Please provide the correct number of arguments")


def main():
    # Accept the number of bitcoin(s) a user wants to buy as cmd arg
    num_of_coins = num_bit_coin()

    # Get price of n bit coin
    total_price = get_price(num_of_coins)
    print(f'${total_price:,.4f}')

def num_bit_coin():
    try:
        return float(sys.argv[1])
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")


def get_price(num_coins):
    # Get response
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("Request not found")

    # Extract the price of one bit coin in usd
    o = response.json()
    results = o['bpi']
    info_usd = results['USD']
    price_usd = info_usd['rate_float']

    return num_coins*price_usd


if __name__ == "__main__":
    main()
