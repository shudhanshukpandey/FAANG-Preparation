"""Builder Pattern: Step-by-step construction of complex objects with fluent chaining."""

from typing import Dict, Any, Optional
import json


# Product
class HTTPRequest:
    def __init__(self) -> None:
        self.method: str = "GET"
        self.url: str = ""
        self.headers: Dict[str, str] = {}
        self.query_params: Dict[str, str] = {}
        self.body: Optional[str] = None
        self.timeout_seconds: int = 30

    def __repr__(self) -> str:
        return (
            f"HTTPRequest(\n"
            f"  method={self.method!r},\n"
            f"  url={self.url!r},\n"
            f"  headers={self.headers},\n"
            f"  params={self.query_params},\n"
            f"  body={self.body},\n"
            f"  timeout={self.timeout_seconds}s\n"
            f")"
        )


# Builder Interface & Concrete Builder
class HTTPRequestBuilder:
    def __init__(self) -> None:
        self._request = HTTPRequest()

    def set_method(self, method: str) -> "HTTPRequestBuilder":
        self._request.method = method.upper()
        return self

    def set_url(self, url: str) -> "HTTPRequestBuilder":
        self._request.url = url
        return self

    def add_header(self, key: str, value: str) -> "HTTPRequestBuilder":
        self._request.headers[key] = value
        return self

    def add_query_param(self, key: str, value: str) -> "HTTPRequestBuilder":
        self._request.query_params[key] = value
        return self

    def set_json_body(self, payload: Dict[str, Any]) -> "HTTPRequestBuilder":
        self._request.body = json.dumps(payload)
        self._request.headers["Content-Type"] = "application/json"
        return self

    def set_timeout(self, seconds: int) -> "HTTPRequestBuilder":
        self._request.timeout_seconds = seconds
        return self

    def build(self) -> HTTPRequest:
        if not self._request.url:
            raise ValueError("URL cannot be empty when building HTTPRequest.")
        # Return built product and reset builder
        product = self._request
        self._request = HTTPRequest()
        return product


if __name__ == "__main__":
    # Fluent API construction
    request = (
        HTTPRequestBuilder()
        .set_method("POST")
        .set_url("https://api.payments.com/v1/charges")
        .add_header("Authorization", "Bearer sk_test_51Mz...")
        .add_query_param("idempotency_key", "idem-uuid-992")
        .set_json_body({"amount": 4999, "currency": "usd", "customer": "cus_991"})
        .set_timeout(10)
        .build()
    )

    print(request)
