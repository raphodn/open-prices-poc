import re
from datetime import datetime


def get_choice_key(choices, value):
    choices = dict(choices)
    for key in choices:
        if choices[key] == value:
            return key
    return None


def format_elefan_product_for_supabase(elefan_product_json):
    return {
        "product_name": elefan_product_json["designation"],
        "product_category": elefan_product_json["famille"]["nom"],
        "product_quantity": elefan_product_json["qte_kg_litre"] if elefan_product_json["qte_kg_litre"] else "",
        "product_code": str(elefan_product_json["code"]),
        # "product_source": "food",
        "price": elefan_product_json["prix_vente"],
        "currency": "€",
        "location": "L'éléfàn, Grenoble",
        "date": datetime.today().strftime("%Y-%m-%d"),
    }


def remove_html_tags(text):
    """
    Remove html tags from a string
    https://medium.com/@jorlugaqui/how-to-strip-html-tags-from-a-string-in-python-7cb81a2bbf44
    """
    clean = re.compile("<.*?>")
    return re.sub(clean, "", text)


def truncate_with_ellipsis(text, ellipsis_threshold=None, ellipsis_string="…"):  # "(…)"
    if ellipsis_threshold and len(text) > ellipsis_threshold:
        text = text[: (ellipsis_threshold - len(ellipsis_string))] + f" {ellipsis_string}"
    return text
