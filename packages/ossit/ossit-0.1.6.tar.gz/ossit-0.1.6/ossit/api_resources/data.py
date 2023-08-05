from datetime import date

from django.utils.timezone import localdate

from ..api_requestor import APIRequestor
from urllib.parse import quote


class Data(APIRequestor):
    @classmethod
    def get_list(cls, group_name, data_name, start_date: date, end_date: date):
        encoded_group_name = quote(group_name)
        encoded_data_name = quote(data_name)
        encoded_start_date = quote(start_date.strftime('%Y-%m-%d'))
        encoded_end_date = quote(end_date.strftime('%Y-%m-%d'))

        return cls.get_request(f'data/list/{encoded_group_name}/{encoded_data_name}/{encoded_start_date}/{encoded_end_date}')

    @classmethod
    def enter(cls, group_name, data_name, value, reference_date: date = None, method_type: str = 'set'):
        encoded_group_name = quote(group_name)
        encoded_data_name = quote(data_name)
        encoded_value = quote(str(value))
        encoded_reference_date = quote(reference_date.strftime('%Y-%m-%d')) if reference_date else localdate().strftime('%Y-%m-%d')
        encoded_method_type = quote(method_type)

        return cls.get_request(f'data/{encoded_group_name}/{encoded_data_name}?value={encoded_value}&reference_date={encoded_reference_date}&method_type={encoded_method_type}')


class Group(APIRequestor):
    @classmethod
    def get_list(cls):
        return cls.get_request('groups/list')

    @classmethod
    def get_detail(cls, group_name):
        return cls.get_request(f'groups/{quote(group_name)}')
