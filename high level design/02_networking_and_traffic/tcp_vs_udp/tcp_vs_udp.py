"""TCP vs UDP Protocol Simulation."""
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Packet:
    seq_num: int
    payload: str

class TCPSocket:
    def __init__(self):
        self.state = "CLOSED"
        self.buffer = {}
        self.expected = 0
    def handshake(self):
        self.state = "ESTABLISHED"
        return ["SYN", "SYN-ACK", "ACK"]
    def receive(self, p: Packet) -> Optional[str]:
        self.buffer[p.seq_num] = p.payload
        out = []
        while self.expected in self.buffer:
            out.append(self.buffer.pop(self.expected))
            self.expected += 1
        return "".join(out) if out else None

class UDPSocket:
    def send(self, payload: str, drop: bool = False) -> bool:
        return not drop

def run_tests():
    tcp = TCPSocket()
    assert tcp.handshake() == ["SYN", "SYN-ACK", "ACK"]
    assert tcp.receive(Packet(1, "World")) is None
    assert tcp.receive(Packet(0, "Hello ")) == "Hello World"
    udp = UDPSocket()
    assert udp.send("A", False) is True
    assert udp.send("B", True) is False
    print("✅ tcp_vs_udp passed!")

if __name__ == "__main__":
    run_tests()
