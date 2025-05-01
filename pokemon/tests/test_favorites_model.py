import unittest
from pokemon.models.favorites_model import FavoritesModel

class TestFavoritesModel(unittest.TestCase):
    def setUp(self):
        """Set up test cases."""
        self.model = FavoritesModel()
        self.test_user_id = "test_user_123"
        self.test_pokemon = {
            "name": "pikachu",
            "id": 25,
            "types": ["electric"]
        }
    
    def test_add_favorite(self):
        """Test adding a favorite Pokemon."""
        success = self.model.add_favorite(self.test_user_id, self.test_pokemon)
        self.assertTrue(success)
        favorites = self.model.get_favorites(self.test_user_id)
        self.assertEqual(len(favorites), 1)
        self.assertEqual(favorites[0]["name"], "pikachu")
    
    def test_remove_favorite(self):
        """Test removing a favorite Pokemon."""
        self.model.add_favorite(self.test_user_id, self.test_pokemon)
        success = self.model.remove_favorite(self.test_user_id, 25)
        self.assertTrue(success)
        favorites = self.model.get_favorites(self.test_user_id)
        self.assertEqual(len(favorites), 0)
    
    def test_get_favorites(self):
        """Test getting user's favorite Pokemon."""
        self.model.add_favorite(self.test_user_id, self.test_pokemon)
        self.model.add_favorite(self.test_user_id, {"name": "charizard", "id": 6, "types": ["fire", "flying"]})
        favorites = self.model.get_favorites(self.test_user_id)
        self.assertEqual(len(favorites), 2)
        self.assertEqual(favorites[0]["name"], "pikachu")
        self.assertEqual(favorites[1]["name"], "charizard")
    
    def test_duplicate_favorite(self):
        """Test adding a duplicate favorite Pokemon."""
        self.model.add_favorite(self.test_user_id, self.test_pokemon)
        success = self.model.add_favorite(self.test_user_id, self.test_pokemon)
        self.assertFalse(success)
        favorites = self.model.get_favorites(self.test_user_id)
        self.assertEqual(len(favorites), 1)
    
    def test_remove_nonexistent_favorite(self):
        """Test removing a favorite Pokemon that doesn't exist."""
        success = self.model.remove_favorite(self.test_user_id, 999)
        self.assertFalse(success)
    
    def test_get_favorites_empty(self):
        """Test getting favorites for a user with no favorites."""
        favorites = self.model.get_favorites(self.test_user_id)
        self.assertEqual(len(favorites), 0)
    
    def test_multiple_users(self):
        """Test handling favorites for multiple users."""
        user2_id = "test_user_456"
        self.model.add_favorite(self.test_user_id, self.test_pokemon)
        self.model.add_favorite(user2_id, {"name": "bulbasaur", "id": 1, "types": ["grass", "poison"]})
        
        user1_favorites = self.model.get_favorites(self.test_user_id)
        user2_favorites = self.model.get_favorites(user2_id)
        
        self.assertEqual(len(user1_favorites), 1)
        self.assertEqual(len(user2_favorites), 1)
        self.assertEqual(user1_favorites[0]["name"], "pikachu")
        self.assertEqual(user2_favorites[0]["name"], "bulbasaur")

if __name__ == '__main__':
    unittest.main() 