from typing import Dict, List, Optional
import logging
from dataclasses import dataclass
from datetime import datetime

logger = logging.getLogger(__name__)

@dataclass
class PokemonStats:
    """Data class for Pokemon stats."""
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int

@dataclass
class PokemonType:
    """Data class for Pokemon type."""
    name: str
    url: str

class PokemonModel:
    """Model for handling Pokemon data and caching."""
    
    def __init__(self):
        """Initialize the Pokemon model."""
        self._cache: Dict[str, Dict] = {}  # name/id -> pokemon data
        self._last_updated: Dict[str, datetime] = {}  # name/id -> last update time
        self._cache_duration = 3600  # Cache duration in seconds (1 hour)
    
    def _is_cache_valid(self, key: str) -> bool:
        """Check if the cached data is still valid.
        
        Args:
            key (str): The cache key (Pokemon name or ID)
            
        Returns:
            bool: True if cache is valid, False otherwise
        """
        if key not in self._last_updated:
            return False
            
        age = (datetime.now() - self._last_updated[key]).total_seconds()
        return age < self._cache_duration
    
    def get_pokemon(self, name_or_id: str) -> Optional[Dict]:
        """Get Pokemon data from cache if available and valid.
        
        Args:
            name_or_id (str): The Pokemon name or ID
            
        Returns:
            Optional[Dict]: Pokemon data if in cache and valid, None otherwise
        """
        if name_or_id in self._cache and self._is_cache_valid(name_or_id):
            logger.info(f"Retrieved {name_or_id} from cache")
            return self._cache[name_or_id]
        return None
    
    def cache_pokemon(self, name_or_id: str, data: Dict) -> None:
        """Cache Pokemon data.
        
        Args:
            name_or_id (str): The Pokemon name or ID
            data (Dict): The Pokemon data to cache
        """
        self._cache[name_or_id] = data
        self._last_updated[name_or_id] = datetime.now()
        logger.info(f"Cached data for {name_or_id}")
    
    def clear_cache(self) -> None:
        """Clear the entire cache."""
        self._cache.clear()
        self._last_updated.clear()
        logger.info("Cleared Pokemon cache")
    
    def remove_from_cache(self, name_or_id: str) -> None:
        """Remove a Pokemon from the cache.
        
        Args:
            name_or_id (str): The Pokemon name or ID to remove
        """
        if name_or_id in self._cache:
            del self._cache[name_or_id]
            del self._last_updated[name_or_id]
            logger.info(f"Removed {name_or_id} from cache")
    
    def get_cache_stats(self) -> Dict:
        """Get cache statistics.
        
        Returns:
            Dict: Cache statistics including size and age of oldest entry
        """
        if not self._cache:
            return {
                "size": 0,
                "oldest_entry_age": 0
            }
            
        oldest_age = min(
            (datetime.now() - timestamp).total_seconds()
            for timestamp in self._last_updated.values()
        )
        
        return {
            "size": len(self._cache),
            "oldest_entry_age": oldest_age
        }
