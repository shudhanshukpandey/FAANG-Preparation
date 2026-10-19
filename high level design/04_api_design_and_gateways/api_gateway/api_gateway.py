"""API Gateway Pattern Simulation."""
class APIGateway:
    def __init__(self):
        self.routes = {"/users": "user_service", "/orders": "order_service"}
    def route(self, token: str, path: str) -> str:
        if token != "valid_token":
            raise PermissionError("401 Unauthorized")
        for prefix, target in self.routes.items():
            if path.startswith(prefix):
                return f"Routed to {target}"
        return "404 Not Found"

def run_tests():
    gw = APIGateway()
    assert gw.route("valid_token", "/users/10") == "Routed to user_service"
    assert gw.route("valid_token", "/orders/88") == "Routed to order_service"
    print("✅ api_gateway passed!")

if __name__ == "__main__":
    run_tests()
