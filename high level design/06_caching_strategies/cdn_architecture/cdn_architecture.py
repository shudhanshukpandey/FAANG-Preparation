"""CDN Edge PoP & Origin Shield Simulation."""
class CDNEngine:
    def __init__(self):
        self.edge_pop_cache = {}
        self.origin = {"/hero.jpg": "image_bytes_4k"}
    def fetch(self, asset: str) -> str:
        if asset not in self.edge_pop_cache:
            self.edge_pop_cache[asset] = self.origin[asset]
        return self.edge_pop_cache[asset]

def run_tests():
    cdn = CDNEngine()
    assert "/hero.jpg" not in cdn.edge_pop_cache
    assert cdn.fetch("/hero.jpg") == "image_bytes_4k"
    assert "/hero.jpg" in cdn.edge_pop_cache # Cached at edge PoP
    print("✅ cdn_architecture passed!")

if __name__ == "__main__":
    run_tests()
