"""Distributed Tracing Context Propagation Simulation."""
class TraceContext:
    def __init__(self, trace_id: str, span_id: str):
        self.trace_id = trace_id
        self.span_id = span_id

class ServiceNode:
    def process(self, parent_ctx: TraceContext, next_span_id: str) -> TraceContext:
        # Propagate trace_id, create child span
        return TraceContext(parent_ctx.trace_id, next_span_id)

def run_tests():
    root_ctx = TraceContext("trace_abc_123", "span_root")
    svc = ServiceNode()
    child_ctx = svc.process(root_ctx, "span_order_service")
    assert child_ctx.trace_id == "trace_abc_123"
    assert child_ctx.span_id == "span_order_service"
    print("✅ distributed_tracing_and_metrics passed!")

if __name__ == "__main__":
    run_tests()
