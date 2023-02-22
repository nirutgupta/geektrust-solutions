import requests


def get_json_from_url(url):
    response = requests.get(url)
    return response.json()


def limit_float_decimal_points(float_number, limit):
    return f'{float_number: .{limit}f}'
