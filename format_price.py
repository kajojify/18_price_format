import argparse


def get_formatted_price(price_string):
    price = float(price_string.replace(',', '.'))
    if price.is_integer():
        price_formatted = "{:,.0f}".format(price)
    else:
        price_formatted = "{:,.2f}".format(price)
    return price_formatted.replace(',', ' ')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Price formatter")
    parser.add_argument("price_string", help="the price you want to format")
    args = parser.parse_args()
    try:
        pretty_price = get_formatted_price(args.price_string)
    except ValueError as error:
        print("Something went wrong!", error)
        exit("Exiting...")
    print(pretty_price)
    
