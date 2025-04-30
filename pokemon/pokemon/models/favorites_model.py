from typing import Dict, List, Optional
import logging

logger = logging.getLogger(__name__)

class FavoritesModel:
    """In-memory model for storing user's favorite Pokemon."""
    
    def __init__(self):
        """Initialize the favorites model."""
        self._favorites: Dict[str, List[Dict]] = {}  # username -> list of favorite pokemon
    
    def add_favorite(self, username: str, pokemon: Dict) -> bool:
        """Add a Pokemon to a user's favorites.
        
        Args:
            username (str): The username
            pokemon (Dict): The Pokemon data to add
            
        Returns:
            bool: True if added successfully, False if already exists
        """
        if username not in self._favorites:
            self._favorites[username] = []
            
        # Check if Pokemon already in favorites
        if any(p['id'] == pokemon['id'] for p in self._favorites[username]):
            logger.info(f"Pokemon {pokemon['name']} already in favorites for {username}")
            return False
            
        self._favorites[username].append(pokemon)
        logger.info(f"Added {pokemon['name']} to favorites for {username}")
        return True
    
    def remove_favorite(self, username: str, pokemon_id: int) -> bool:
        """Remove a Pokemon from a user's favorites.
        
        Args:
            username (str): The username
            pokemon_id (int): The ID of the Pokemon to remove
            
        Returns:
            bool: True if removed successfully, False if not found
        """
        if username not in self._favorites:
            return False
            
        initial_length = len(self._favorites[username])
        self._favorites[username] = [p for p in self._favorites[username] if p['id'] != pokemon_id]
        
        if len(self._favorites[username]) < initial_length:
            logger.info(f"Removed Pokemon {pokemon_id} from favorites for {username}")
            return True
        return False
    
    def get_favorites(self, username: str) -> List[Dict]:
        """Get all favorite Pokemon for a user.
        
        Args:
            username (str): The username
            
        Returns:
            List[Dict]: List of favorite Pokemon
        """
        return self._favorites.get(username, [])
    
    def is_favorite(self, username: str, pokemon_id: int) -> bool:
        """Check if a Pokemon is in a user's favorites.
        
        Args:
            username (str): The username
            pokemon_id (int): The ID of the Pokemon to check
            
        Returns:
            bool: True if the Pokemon is in favorites, False otherwise
        """
        if username not in self._favorites:
            return False
        return any(p['id'] == pokemon_id for p in self._favorites[username])
