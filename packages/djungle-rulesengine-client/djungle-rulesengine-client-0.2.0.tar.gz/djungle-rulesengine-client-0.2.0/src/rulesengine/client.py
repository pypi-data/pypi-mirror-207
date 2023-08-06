import requests
from requests.exceptions import HTTPError


class EngineClientError(Exception):
    pass


class EngineClient:
    def __init__(self, base_url, token, timeout=30):
        self._base_url = base_url
        self._headers = {"X-Auth-Token": token}
        self._timeout = timeout

    def push_action(self, subject_id: str, action: str, payload: dict) -> None:
        endpoint = f"{self._base_url}/api/v1/subjects/{subject_id}/props/?a={action}"
        data = {"payload": payload}
        response = requests.post(endpoint, json=data, headers=self._headers, timeout=self._timeout)
        try:
            response.raise_for_status()
        except HTTPError as e:
            raise EngineClientError from e

    def get_pluggable_props(self, subject_id: str, props: str, **kwargs):
        params = {"p": props, **kwargs}
        endpoint = f"{self._base_url}/api/v1/subjects/{subject_id}/props/"
        response = requests.get(endpoint, headers=self._headers, params=params, timeout=self._timeout)
        try:
            response.raise_for_status()
        except HTTPError as e:
            raise EngineClientError from e
        return response.json()
