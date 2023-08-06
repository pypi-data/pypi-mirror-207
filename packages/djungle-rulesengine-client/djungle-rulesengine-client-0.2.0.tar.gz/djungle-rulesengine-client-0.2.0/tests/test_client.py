from unittest import TestCase

import requests_mock

from rulesengine.client import EngineClient, EngineClientError


class EngineClientTestCase(TestCase):
    @requests_mock.Mocker()
    def test_push_action_success(self, engine_api_mock):
        engine = EngineClient(base_url="https://example.com", token="abcde")
        engine_api_mock.post("https://example.com/api/v1/subjects/sys-1/props/?a=my-action")

        ret = engine.push_action("sys-1", "my-action", {"key": "value"})

        self.assertIsNone(ret)

        request = engine_api_mock.last_request
        self.assertEqual(request.headers["X-Auth-Token"], "abcde")
        self.assertEqual(request.json(), {"payload": {"key": "value"}})

    @requests_mock.Mocker()
    def test_push_action_failure(self, engine_api_mock):
        engine = EngineClient(base_url="https://example.com", token="abcde")
        engine_api_mock.post(
            "https://example.com/api/v1/subjects/sys-1/props/?a=my-action",
            json={"error": "ko"},
            status_code=400,
        )

        with self.assertRaises(EngineClientError) as cm:
            engine.push_action("sys-1", "my-action", {"key": "value"})

        self.assertEqual(cm.exception.__cause__.response.json(), {"error": "ko"})

        request = engine_api_mock.last_request
        self.assertEqual(request.headers["X-Auth-Token"], "abcde")
        self.assertEqual(request.json(), {"payload": {"key": "value"}})

    @requests_mock.Mocker()
    def test_get_pluggable_props_success(self, engine_api_mock):
        engine = EngineClient(base_url="https://example.com", token="abcde")
        engine_api_mock.get(
            "https://example.com/api/v1/subjects/sys-1/props/?p=my-prop", json={"status": "ok"}
        )

        ret = engine.get_pluggable_props("sys-1", "my-prop")

        self.assertEqual(ret, {"status": "ok"})

        request = engine_api_mock.last_request
        self.assertEqual(request.headers["X-Auth-Token"], "abcde")

    @requests_mock.Mocker()
    def test_get_pluggable_props_failure(self, engine_api_mock):
        engine = EngineClient(base_url="https://example.com", token="abcde")
        engine_api_mock.get(
            "https://example.com/api/v1/subjects/sys-1/props/?p=my-prop&key=value",
            json={"error": "ko"},
            status_code=400,
        )

        with self.assertRaises(EngineClientError) as cm:
            engine.get_pluggable_props("sys-1", "my-prop", key="value")

        self.assertEqual(cm.exception.__cause__.response.json(), {"error": "ko"})

        request = engine_api_mock.last_request
        self.assertEqual(request.headers["X-Auth-Token"], "abcde")
