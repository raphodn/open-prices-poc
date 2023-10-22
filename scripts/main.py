import sys

from common.api import elefan, openfoodfacts, supabase
from common.utils import format_elefan_product_for_supabase


code = "8000215204219"


def send_one_elefan_product_to_supabase_price(product_code):
    elefan_product = elefan.find_product_by_code(product_code)
    elefan_product_formatted = format_elefan_product_for_supabase(elefan_product)
    response = supabase.price_create(elefan_product_formatted)
    print(response)


def send_all_elefan_products_to_supabase_price():
    elefan_products = elefan.get_products_with_valid_code()

    progress = 0
    for elefan_product in elefan_products:
        elefan_product_formatted = format_elefan_product_for_supabase(elefan_product)
        supabase.price_create(elefan_product_formatted)
        progress += 1
        if (progress % 50) == 0:
            print(f"{progress}...")


def check_supabase_product_is_in_openfoodfacts(product_code=None):
    if product_code:
        print(product_code)
        supabase_prices = supabase.price_find_by_product_code(product_code)
    else:
        supabase_prices = supabase.price_all()
    print(len(supabase_prices))

    progress = 0
    for supabase_price in supabase_prices:
        # print(supabase_price)
        try:
            openfoodfacts.get_product(supabase_price["product_code"])
            supabase.price_update(supabase_price["id"], {"in_off": True})
        except:  # noqa
            supabase.price_update(supabase_price["id"], {"in_off": False})
        progress += 1
        if (progress % 50) == 0:
            print(f"{progress}...")


def main():
    # send_one_elefan_product_to_supabase_price(code)
    # send_all_elefan_products_to_supabase_price()
    # check_supabase_product_is_in_openfoodfacts()
    check_supabase_product_is_in_openfoodfacts(product_code=code)


if __name__ == "__main__":
    sys.exit(main())
