"""LLM Continuous Batching & KV-Cache Management Simulation."""
class ContinuousBatcher:
    def __init__(self, max_batch_size=4):
        self.max_batch_size = max_batch_size
        self.active_requests = {}
        self.kv_cache_allocated = 0

    def add_request(self, req_id: str, prompt_tokens: int):
        self.active_requests[req_id] = {"tokens": prompt_tokens, "generated": 0}
        self.kv_cache_allocated += prompt_tokens

    def step(self) -> dict[str, str]:
        emitted = {}
        for rid, req in list(self.active_requests.items()):
            req["generated"] += 1
            self.kv_cache_allocated += 1
            emitted[rid] = f"token_{req['generated']}"
            if req["generated"] >= 3: # Finished request
                self.kv_cache_allocated -= (req["tokens"] + req["generated"])
                del self.active_requests[rid]
        return emitted

def run_tests():
    cb = ContinuousBatcher(4)
    cb.add_request("req1", 10)
    tokens_1 = cb.step()
    assert "req1" in tokens_1
    cb.add_request("req2", 5) # Dynamically joins next iteration!
    tokens_2 = cb.step()
    assert "req1" in tokens_2 and "req2" in tokens_2
    print("✅ llm_inference_serving passed!")

if __name__ == "__main__":
    run_tests()
