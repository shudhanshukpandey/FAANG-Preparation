"""Middleware Pipeline Pattern: ASGI/WSGI onion architecture for HTTP requests."""

import time
import uuid
from typing import Callable, Dict, Any


# Standard signature: (request, call_next) -> response
Handler = Callable[[Dict[str, Any]], Dict[str, Any]]
Middleware = Callable[[Dict[str, Any], Handler], Dict[str, Any]]


# 1. Concrete Middleware 1: Distributed Tracing Middleware (Injects X-Request-ID)
def request_id_middleware(request: Dict[str, Any], call_next: Handler) -> Dict[str, Any]:
    req_id = request.get("headers", {}).get("X-Request-ID", str(uuid.uuid4())[:8])
    request["request_id"] = req_id
    print(f"[Trace Middleware -> IN] Inbound request tagged with ID: {req_id}")

    response = call_next(request)

    response["headers"]["X-Request-ID"] = req_id
    print(f"[Trace Middleware <- OUT] Outbound response tagged with ID: {req_id}")
    return response


# 2. Concrete Middleware 2: Timing Middleware (Calculates latency)
def timing_middleware(request: Dict[str, Any], call_next: Handler) -> Dict[str, Any]:
    start_time = time.time()
    print("[Timing Middleware -> IN] Started request timer.")

    response = call_next(request)

    duration_ms = (time.time() - start_time) * 1000
    response["headers"]["X-Response-Time-Ms"] = f"{duration_ms:.2f}ms"
    print(f"[Timing Middleware <- OUT] Completed in {duration_ms:.2f}ms.")
    return response


# 3. Concrete Middleware 3: Error Handling Middleware
def error_handling_middleware(request: Dict[str, Any], call_next: Handler) -> Dict[str, Any]:
    try:
        return call_next(request)
    except Exception as exc:
        print(f"[Error Middleware] Caught uncaught exception: {exc}")
        return {
            "status_code": 500,
            "headers": {},
            "body": {"error": "InternalServerError", "message": str(exc)}
        }


# 4. Target Endpoint / Router Handler
def mock_api_endpoint(request: Dict[str, Any]) -> Dict[str, Any]:
    print(f"  [API Handler] Executing business logic for path: {request.get('path')}...")
    if request.get("fail"):
        raise RuntimeError("Database connection timed out!")
    return {
        "status_code": 200,
        "headers": {"Content-Type": "application/json"},
        "body": {"message": "Success", "user": "alice"}
    }


# 5. Pipeline Assembler (Onion wrapper)
class MiddlewarePipeline:
    def __init__(self, endpoint_handler: Handler) -> None:
        self.endpoint = endpoint_handler
        self.middlewares: list[Middleware] = []

    def add_middleware(self, middleware: Middleware) -> None:
        self.middlewares.append(middleware)

    def execute(self, request: Dict[str, Any]) -> Dict[str, Any]:
        # Wrap middlewares from inside out (onion)
        chained_handler = self.endpoint
        for mw in reversed(self.middlewares):
            prev_handler = chained_handler

            def make_handler(m=mw, n=prev_handler):
                return lambda req: m(req, n)

            chained_handler = make_handler()

        return chained_handler(request)


if __name__ == "__main__":
    app = MiddlewarePipeline(mock_api_endpoint)
    # Order matters: Outermost -> Innermost
    app.add_middleware(error_handling_middleware)
    app.add_middleware(request_id_middleware)
    app.add_middleware(timing_middleware)

    print("--- 1. Executing Normal Request ---")
    req = {"path": "/api/v1/profile", "headers": {}}
    res = app.execute(req)
    print("Final HTTP Response:", res)

    print("\n--- 2. Executing Failing Request (Handled Gracefully by Error Middleware) ---")
    fail_req = {"path": "/api/v1/crash", "headers": {}, "fail": True}
    res_fail = app.execute(fail_req)
    print("Final HTTP Response:", res_fail)
