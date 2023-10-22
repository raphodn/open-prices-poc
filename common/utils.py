from datetime import datetime


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
