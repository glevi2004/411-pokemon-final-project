# Pokemon API Project

## Overview
A Flask-based web application that allows users to interact with Pokemon data from the PokeAPI. Users can create accounts, search for Pokemon, manage their favorite Pokemon, and view evolution chains. The application demonstrates secure user authentication, external API integration, and in-memory data management.

## Features
- User Authentication (Create account, Login, Logout, Update password)
- Pokemon Information Retrieval
- Favorite Pokemon Management
- Evolution Chain Viewing
- Secure Password Storage using SQLite
- In-Memory Data Caching

## Tech Stack
- **Backend**: Flask 3.0.3
- **Database**: SQLite (via SQLAlchemy)
- **Authentication**: Flask-Login
- **External API**: PokeAPI
- **Other Dependencies**: 
  - Flask-Cors 4.0.1
  - Flask-SQLAlchemy 3.1.1
  - python-dotenv 1.0.1
  - requests 2.32.3

## API Routes Documentation

### Health Check
**Route**: `/healthcheck`
- **Request Type**: GET
- **Purpose**: Verify API health
- **Response Format**: JSON
  ```json
  {
    "status": "healthy",
    "message": "Pokemon API is running"
  }
  ```

### User Management

#### Create Account
**Route**: `/create-account`
- **Request Type**: PUT
- **Purpose**: Creates a new user account
- **Request Body**:
  ```json
  {
    "username": "trainer123",
    "password": "secure_password"
  }
  ```
- **Response Format**:
  ```json
  {
    "status": "success",
    "message": "Account created successfully"
  }
  ```

#### Login
**Route**: `/login`
- **Request Type**: POST
- **Purpose**: Authenticates user and creates session
- **Request Body**:
  ```json
  {
    "username": "trainer123",
    "password": "secure_password"
  }
  ```
- **Response Format**:
  ```json
  {
    "status": "success",
    "message": "Logged in successfully"
  }
  ```

### Pokemon Management

#### Get Pokemon Details
**Route**: `/pokemon/<name_or_id>`
- **Request Type**: GET
- **Purpose**: Retrieves detailed information about a specific Pokemon
- **Response Format**:
  ```json
  {
    "id": 25,
    "name": "pikachu",
    "types": ["electric"],
    "stats": {
      "hp": 35,
      "attack": 55,
      "defense": 40,
      "special-attack": 50,
      "special-defense": 50,
      "speed": 90
    }
  }
  ```

#### Manage Favorites
**Route**: `/favorites`
- **Request Type**: GET
- **Purpose**: Retrieves user's favorite Pokemon
- **Response Format**:
  ```json
  {
    "status": "success",
    "favorites": [
      {
        "id": 25,
        "name": "pikachu",
        "types": ["electric"]
      }
    ]
  }
  ```

**Route**: `/favorites`
- **Request Type**: POST
- **Purpose**: Adds a Pokemon to favorites
- **Request Body**:
  ```json
  {
    "pokemon_id": 25
  }
  ```
- **Response Format**:
  ```json
  {
    "status": "success",
    "message": "Added pikachu to favorites"
  }
  ```

**Route**: `/favorites/<pokemon_id>`
- **Request Type**: DELETE
- **Purpose**: Removes a Pokemon from favorites
- **Response Format**:
  ```json
  {
    "status": "success",
    "message": "Pokemon removed from favorites"
  }
  ```

#### Evolution Chain
**Route**: `/evolutions/<pokemon_id>`
- **Request Type**: GET
- **Purpose**: Retrieves evolution chain for a Pokemon
- **Response Format**:
  ```json
  {
    "chain": {
      "species": "pichu",
      "evolves_to": [
        {
          "species": "pikachu",
          "evolves_to": [
            {
              "species": "raichu"
            }
          ]
        }
      ]
    }
  }
  ```

## Testing
The project includes unit tests and smoke tests. To run tests:

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/test_pokemon_model.py -v

# Run smoke tests
python smoketest.py
```

## Project Structure
```
pokemon/
├── pokemon/
│   ├── models/
│   │   ├── pokemon_model.py
│   │   ├── favorites_model.py
│   │   └── user_model.py
│   ├── utils/
│   │   ├── api_utils.py
│   │   └── logger.py
│   ├── app.py
│   └── routes.py
├── tests/
│   ├── test_pokemon_model.py
│   ├── test_favorites_model.py
│   └── test_user_model.py
├── sql/
│   ├── create_db.sh
│   └── init_db.sql
├── Dockerfile
├── requirements.txt
└── smoketest.py
```

## License
This project is licensed under the MIT License. 