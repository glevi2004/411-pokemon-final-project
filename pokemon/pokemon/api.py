import requests
import logging
from typing import Dict, List, Optional, Union

logger = logging.getLogger(__name__)

class PokemonAPI:
    """Wrapper for the PokeAPI (https://pokeapi.co/)"""
    
    BASE_URL = "https://pokeapi.co/api/v2"
    
    def __init__(self):
        """Initialize the Pokemon API wrapper."""
        self.session = requests.Session()
    
    def _make_request(self, endpoint: str) -> Dict:
        """Make a request to the PokeAPI.
        
        Args:
            endpoint (str): The API endpoint to call
            
        Returns:
            Dict: The JSON response from the API
            
        Raises:
            requests.exceptions.RequestException: If the request fails
        """
        try:
            response = self.session.get(f"{self.BASE_URL}/{endpoint}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error making request to {endpoint}: {str(e)}")
            raise
    
    def get_pokemon(self, name_or_id: Union[str, int]) -> Dict:
        """Get information about a specific Pokemon.
        
        Args:
            name_or_id (Union[str, int]): The name or ID of the Pokemon
            
        Returns:
            Dict: Pokemon information including name, types, abilities, and stats
        """
        return self._make_request(f"pokemon/{name_or_id}")
    
    def get_evolution_chain(self, id: int) -> Dict:
        """Get the evolution chain for a Pokemon.
        
        Args:
            id (int): The ID of the Pokemon
            
        Returns:
            Dict: Evolution chain information
        """
        return self._make_request(f"evolution-chain/{id}")
    
    def search_pokemon(self, query: str) -> List[Dict]:
        """Search for Pokemon by name.
        
        Args:
            query (str): The search query
            
        Returns:
            List[Dict]: List of matching Pokemon
        """
        # Note: PokeAPI doesn't have a direct search endpoint
        # We'll need to implement this using the pokemon list endpoint
        # and filtering the results
        pass