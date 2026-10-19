"""Kappa Architecture (Single Stream Engine) Simulation."""
class KappaPipeline:
    def __init__(self):
        self.stream_log = []
        self.serving_view = {}
    def ingest(self, key: str, val: int):
        self.stream_log.append((key, val))
        self.serving_view[key] = self.serving_view.get(key, 0) + val
    def recompute(self):
        """Reprocessing historical data by replaying Kafka log."""
        self.serving_view = {}
        for k, v in self.stream_log:
            self.serving_view[k] = self.serving_view.get(k, 0) + v

def run_tests():
    kp = KappaPipeline()
    kp.ingest("user_clicks", 10)
    kp.ingest("user_clicks", 15)
    assert kp.serving_view["user_clicks"] == 25
    kp.recompute()
    assert kp.serving_view["user_clicks"] == 25
    print("✅ lambda_vs_kappa_architecture passed!")

if __name__ == "__main__":
    run_tests()
