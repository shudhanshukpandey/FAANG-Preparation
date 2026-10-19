"""Deployment Router (Canary Split Simulation)."""
class DeploymentRouter:
    def __init__(self, canary_weight=0.10):
        self.canary_weight = canary_weight
    def route_request(self, user_hash: int) -> str:
        # user_hash normalized between 0.0 and 1.0
        return "CANARY_V2" if user_hash < self.canary_weight else "STABLE_V1"

def run_tests():
    dr = DeploymentRouter(0.10)
    assert dr.route_request(0.05) == "CANARY_V2"
    assert dr.route_request(0.50) == "STABLE_V1"
    print("✅ deployment_strategies passed!")

if __name__ == "__main__":
    run_tests()
