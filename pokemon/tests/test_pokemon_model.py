import unittest
from datetime import datetime, timedelta
from pokemon.models.pokemon_model import PokemonModel, PokemonStats, PokemonType

class TestPokemonModel(unittest.TestCase):
    def setUp(self):
        """Set up test cases."""
        self.model = PokemonModel()
        self.test_pokemon = {
            "name": "pikachu",
            "id": 25,
            "types": [
                {"type": {"name": "electric", "url": "https://pokeapi.co/api/v2/type/13/"}}
            ],
            "stats": [
                {"base_stat": 35, "stat": {"name": "hp"}},
                {"base_stat": 55, "stat": {"name": "attack"}},
                {"base_stat": 40, "stat": {"name": "defense"}},
                {"base_stat": 50, "stat": {"name": "special-attack"}},
                {"base_stat": 50, "stat": {"name": "special-defense"}},
                {"base_stat": 90, "stat": {"name": "speed"}}
            ]
        }
    
    def test_cache_pokemon(self):
        """Test caching Pokemon data."""
        self.model.cache_pokemon("pikachu", self.test_pokemon)
        cached = self.model.get_pokemon("pikachu")
        self.assertEqual(cached, self.test_pokemon)
    
    def test_cache_expiration(self):
        """Test cache expiration."""
        self.model.cache_pokemon("pikachu", self.test_pokemon)
        # Manually expire the cache
        self.model._last_updated["pikachu"] = datetime.now() - timedelta(hours=2)
        cached = self.model.get_pokemon("pikachu")
        self.assertIsNone(cached)
    
    def test_clear_cache(self):
        """Test clearing the cache."""
        self.model.cache_pokemon("pikachu", self.test_pokemon)
        self.model.cache_pokemon("charizard", {"name": "charizard"})
        self.model.clear_cache()
        self.assertIsNone(self.model.get_pokemon("pikachu"))
        self.assertIsNone(self.model.get_pokemon("charizard"))
    
    def test_remove_from_cache(self):
        """Test removing a specific Pokemon from cache."""
        self.model.cache_pokemon("pikachu", self.test_pokemon)
        self.model.cache_pokemon("charizard", {"name": "charizard"})
        self.model.remove_from_cache("pikachu")
        self.assertIsNone(self.model.get_pokemon("pikachu"))
        self.assertIsNotNone(self.model.get_pokemon("charizard"))
    
    def test_get_cache_stats(self):
        """Test getting cache statistics."""
        self.model.cache_pokemon("pikachu", self.test_pokemon)
        stats = self.model.get_cache_stats()
        self.assertEqual(stats["size"], 1)
        self.assertLess(stats["oldest_entry_age"], 1)  # Should be very recent
    
    def test_empty_cache_stats(self):
        """Test cache statistics for empty cache."""
        stats = self.model.get_cache_stats()
        self.assertEqual(stats["size"], 0)
        self.assertEqual(stats["oldest_entry_age"], 0)

if __name__ == '__main__':
    unittest.main() 