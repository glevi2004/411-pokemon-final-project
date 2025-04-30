from flask import Blueprint, jsonify, request, make_response
from flask_login import login_required, current_user
import logging

from pokemon.api import PokemonAPI
from pokemon.models.favorites_model import FavoritesModel

logger = logging.getLogger(__name__)

# Initialize API and models
pokemon_api = PokemonAPI()
favorites_model = FavoritesModel()

# Create blueprint
pokemon_bp = Blueprint('pokemon', __name__)

@pokemon_bp.route('/healthcheck', methods=['GET'])
def healthcheck():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "message": "Pokemon API is running"
    })

@pokemon_bp.route('/pokemon/<name_or_id>', methods=['GET'])
@login_required
def get_pokemon(name_or_id):
    """Get information about a specific Pokemon."""
    try:
        pokemon = pokemon_api.get_pokemon(name_or_id)
        return jsonify(pokemon)
    except Exception as e:
        logger.error(f"Error getting Pokemon {name_or_id}: {str(e)}")
        return make_response(jsonify({
            "status": "error",
            "message": f"Error getting Pokemon: {str(e)}"
        }), 500)

@pokemon_bp.route('/favorites', methods=['GET'])
@login_required
def get_favorites():
    """Get all favorite Pokemon for the current user."""
    favorites = favorites_model.get_favorites(current_user.username)
    return jsonify({
        "status": "success",
        "favorites": favorites
    })

@pokemon_bp.route('/favorites', methods=['POST'])
@login_required
def add_favorite():
    """Add a Pokemon to favorites."""
    data = request.get_json()
    if not data or 'pokemon_id' not in data:
        return make_response(jsonify({
            "status": "error",
            "message": "pokemon_id is required"
        }), 400)
        
    try:
        pokemon = pokemon_api.get_pokemon(data['pokemon_id'])
        if favorites_model.add_favorite(current_user.username, pokemon):
            return jsonify({
                "status": "success",
                "message": f"Added {pokemon['name']} to favorites"
            })
        else:
            return make_response(jsonify({
                "status": "error",
                "message": f"{pokemon['name']} is already in favorites"
            }), 400)
    except Exception as e:
        logger.error(f"Error adding favorite: {str(e)}")
        return make_response(jsonify({
            "status": "error",
            "message": f"Error adding favorite: {str(e)}"
        }), 500)

@pokemon_bp.route('/favorites/<int:pokemon_id>', methods=['DELETE'])
@login_required
def remove_favorite(pokemon_id):
    """Remove a Pokemon from favorites."""
    if favorites_model.remove_favorite(current_user.username, pokemon_id):
        return jsonify({
            "status": "success",
            "message": "Pokemon removed from favorites"
        })
    else:
        return make_response(jsonify({
            "status": "error",
            "message": "Pokemon not found in favorites"
        }), 404)

@pokemon_bp.route('/evolutions/<int:pokemon_id>', methods=['GET'])
@login_required
def get_evolutions(pokemon_id):
    """Get evolution chain for a Pokemon."""
    try:
        evolution_chain = pokemon_api.get_evolution_chain(pokemon_id)
        return jsonify(evolution_chain)
    except Exception as e:
        logger.error(f"Error getting evolution chain: {str(e)}")
        return make_response(jsonify({
            "status": "error",
            "message": f"Error getting evolution chain: {str(e)}"
        }), 500)