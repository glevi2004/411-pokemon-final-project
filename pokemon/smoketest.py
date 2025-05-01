# smoketest.py

import sys
import requests
import random
import string

BASE_URL = "http://localhost:5000"

def assert_status(resp: requests.Response, expected: int):
    if resp.status_code != expected:
        print(f"✗ {resp.request.method} {resp.url} → {resp.status_code} (expected {expected})")
        print("  Response body:", resp.text)
        sys.exit(1)
    else:
        print(f"✓ {resp.request.method} {resp.url} → {resp.status_code}")

def random_username(length=8):
    return "user_" + "".join(random.choices(string.ascii_lowercase + string.digits, k=length))

def main():
    s = requests.Session()

    # 1) Health endpoints
    assert_status(s.get(f"{BASE_URL}/api/health"), 200)
    assert_status(s.get(f"{BASE_URL}/api/healthcheck"), 200)

    # 2) Reset users (start clean)
    assert_status(s.delete(f"{BASE_URL}/api/reset-users"), 200)

    # 3) Create a new user
    username = random_username()
    password = "Test@123"
    print(f"\n-- Creating user: {username}")
    r = s.put(f"{BASE_URL}/api/create-user", json={"username": username, "password": password})
    assert_status(r, 201)

    # 4) Log in
    print(f"\n-- Logging in as {username}")
    r = s.post(f"{BASE_URL}/api/login", json={"username": username, "password": password})
    assert_status(r, 200)

    # 5) Hit a protected resource
    print("\n-- Fetching Pokémon #1")
    r = s.get(f"{BASE_URL}/api/pokemon/1")
    assert_status(r, 200)

    # 6) Favorites workflow
    print("\n-- Adding favorite #1")
    r = s.post(f"{BASE_URL}/api/favorites", json={"pokemon_id": 1})
    assert_status(r, 200)

    print("\n-- Listing favorites")
    r = s.get(f"{BASE_URL}/api/favorites")
    assert_status(r, 200)

    print("\n-- Removing favorite #1")
    r = s.delete(f"{BASE_URL}/api/favorites/1")
    assert_status(r, 200)

    # 7) Evolution chain
    print("\n-- Fetching evolution chain for #1")
    r = s.get(f"{BASE_URL}/api/evolutions/1")
    assert_status(r, 200)

    # 8) Logout
    print("\n-- Logging out")
    r = s.post(f"{BASE_URL}/api/logout")
    assert_status(r, 200)

    print("\n🎉  All smoke tests passed!")
    sys.exit(0)

if __name__ == "__main__":
    main()
