import os
from dotenv import load_dotenv

from supabase import create_client


load_dotenv()


"""
Python API: https://github.com/supabase-community/supabase-py
Documentation: https://supabase.com/docs/reference/python
"""


def get_client():
    return create_client(os.environ.get("SUPABASE_URL"), os.environ.get("SUPABASE_KEY"))


def get_table():
    return os.environ.get("SUPABASE_PRICE_TABLE_NAME")


def price_all():
    client = get_client()
    table = get_table()
    data = client.table(table).select("*").execute()
    return data.data


def price_find_by_product_code(product_code):
    client = get_client()
    table = get_table()
    data = (
        client.table(table).select("*").eq("product_code", str(product_code)).execute()
    )
    print(data.data)
    return data.data


def price_create(price_data):
    client = get_client()
    table = get_table()
    data = client.table(table).insert(price_data).execute()
    return data


def price_update(price_id, price_data):
    client = get_client()
    table = get_table()
    data = client.table(table).update(price_data).eq("id", int(price_id)).execute()
    return data


def price_delete_all():
    client = get_client()
    table = get_table()
    data = client.table(table).delete().gt("id", 0).execute()
    return data
