"""Feature Flag Engine Simulation."""
class FeatureFlagEngine:
    def __init__(self):
        self.flags = {}
    def set_flag(self, flag_name: str, enabled: bool, rollout_pct: float = 1.0):
        self.flags[flag_name] = {"enabled": enabled, "pct": rollout_pct}
    def is_enabled(self, flag_name: str, user_id_hash: float) -> bool:
        f = self.flags.get(flag_name)
        if not f or not f["enabled"]:
            return False
        return user_id_hash <= f["pct"]

def run_tests():
    ff = FeatureFlagEngine()
    ff.set_flag("new_checkout_ui", enabled=True, rollout_pct=0.20)
    assert ff.is_enabled("new_checkout_ui", 0.15) is True
    assert ff.is_enabled("new_checkout_ui", 0.35) is False
    # Kill switch
    ff.set_flag("new_checkout_ui", enabled=False)
    assert ff.is_enabled("new_checkout_ui", 0.10) is False
    print("✅ feature_flags passed!")

if __name__ == "__main__":
    run_tests()
