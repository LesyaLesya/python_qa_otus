import requests
from unittest.mock import Mock


def get_resource(session, base_url, res_id):
    if isinstance(requests.get, Mock):
        r = session.get(res_id)
    else:
        r = session.get(f'{base_url}/{res_id}')
    return r


def get_all_resources(session, base_url):
    if isinstance(requests.get, Mock):
        r = session.get("mock")
    else:
        r = session.get(base_url)
    return r


def delete_resource(session, base_url, res_id):
    if isinstance(requests.delete, Mock):
        r = session.delete(res_id)
    else:
        r = session.delete(f'{base_url}/{res_id}')
    return r


def post_resource_positive(session, base_url, payload):
    if isinstance(requests.post, Mock):
        r = session.post(url="mock", json=payload)
    else:
        r = session.post(url=base_url, json=payload)
    return r


def post_resource_negative(session, base_url, payload, headers):
    if isinstance(requests.post, Mock):
        r = session.post(url="mock", data=payload, headers=headers)
    else:
        r = session.post(url=base_url, data=payload, headers=headers)
    return r


def put_resource(session, base_url, res_id, payload):
    if isinstance(requests.put, Mock):
        r = session.put(url=res_id, json=payload)
    else:
        r = session.put(url=f'{base_url}/{res_id}', json=payload)
    return r


def patch_resource_positive(session, base_url, res_id, payload, headers=None):
    if isinstance(requests.patch, Mock):
        r = session.patch(res_id, headers, json=payload)
    else:
        r = session.patch(f'{base_url}/{res_id}', headers, json=payload)
    return r


def patch_resource_negative(session, base_url, res_id, payload, headers):
    if isinstance(requests.patch, Mock):
        r = session.patch(url="mock", data=payload, headers=headers)
    else:
        r = session.patch(url=f'{base_url}/{res_id}', data=payload, headers=headers)
    return r


def filter_resource_by_id(session, base_url, res_id):
    if isinstance(requests.get, Mock):
        r = session.get(res_id)
    else:
        r = session.get(f'{base_url}?id={res_id}')
    return r


def filter_resource_by_userid(session, base_url, res_id):
    if isinstance(requests.get, Mock):
        r = session.get(res_id)
    else:
        r = session.get(f'{base_url}?userId={res_id}')
    return r


def filter_resource_by_completed(session, base_url, completed):
    if isinstance(requests.get, Mock):
        r = session.get(completed)
    else:
        r = session.get(f'{base_url}?completed={completed}')
    return r


def filter_resource_by_title(session, base_url, title):
    if isinstance(requests.get, Mock):
        r = session.get(title)
    else:
        r = session.get(f'{base_url}?title={title}')
    return r
