import json
from collections import Counter


EXPORT_FILE = "local_data/20231013_elefan_products.json"


def read_json_file(file: str = EXPORT_FILE):
    print("Reading JSON file", file)

    with open(file) as f:
        product_list = f.read()

    product_list_json = json.loads(product_list)

    print(len(product_list_json))

    return product_list_json


def find_product_by_code(code: str):
    print("Looking for product with code", code)

    product_list = read_json_file()
    product = next((product for product in product_list if (product["code"] == code or product["code"] == int(code))), None)

    if not product:
        raise ValueError("Product not found")

    print("Product found")
    return product


def get_products_with_valid_code():
    print("Filtering products with valid code")

    product_list = read_json_file()
    product_list_filtered = list(filter(lambda product: len(str(product["code"])) == 13, product_list))

    # product_list_filtered_categories = [product["famille"]["nom"] for product in product_list_filtered]
    # print(Counter(product_list_filtered_categories))

    print("Found", len(product_list_filtered), "products")
    return product_list_filtered
