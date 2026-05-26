"""
Random Joke Generator
This script fetches random jokes from the JokeAPI and displays them.
"""

import requests
import json
from typing import Dict, Optional


class JokeGenerator:
    """A class to fetch and display random jokes from JokeAPI."""
    
    BASE_URL = "https://v2.jokeapi.dev/joke/"
    
    def __init__(self):
        """Initialize the JokeGenerator with default settings."""
        self.session = requests.Session()
        self.joke_types = ["Any", "Programming", "Knock-Knock", "General"]
    
    def get_random_joke(self, joke_type: str = "Any") -> Optional[Dict]:
        """
        Fetch a random joke from the API.
        
        Args:
            joke_type (str): Type of joke - "Any", "Programming", "Knock-Knock", or "General"
        
        Returns:
            Dict: Joke data if successful, None otherwise
        """
        try:
            url = f"{self.BASE_URL}{joke_type}"
            response = self.session.get(url, timeout=5)
            response.raise_for_status()
            
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching joke: {e}")
            return None
    
    def display_joke(self, joke_data: Dict) -> None:
        """
        Display the joke in a formatted way.
        
        Args:
            joke_data (Dict): The joke data from the API
        """
        if joke_data is None or joke_data.get("error"):
            print("Could not fetch a joke. Please try again.")
            return
        
        print("\n" + "=" * 60)
        
        # Check if it's a single joke or two-part joke
        if joke_data["type"] == "single":
            print(f"Joke: {joke_data['joke']}")
        else:  # two-part
            print(f"Setup: {joke_data['setup']}")
            print(f"\nPunchline: {joke_data['delivery']}")
        
        print(f"\nCategory: {joke_data['category']}")
        print("=" * 60 + "\n")
    
    def get_random_joke_safe(self) -> Optional[Dict]:
        """
        Fetch a random joke with safety flags enabled (no explicit content).
        
        Returns:
            Dict: Safe joke data if successful, None otherwise
        """
        try:
            url = f"{self.BASE_URL}Any?safe-mode"
            response = self.session.get(url, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching safe joke: {e}")
            return None


def main():
    """Main function to demonstrate the JokeGenerator."""
    print("🎭 Welcome to the Random Joke Generator! 🎭")
    print("\nAvailable joke types: Any, Programming, Knock-Knock, General")
    
    generator = JokeGenerator()
    
    while True:
        print("\nOptions:")
        print("1. Get a random joke (Any type)")
        print("2. Get a programming joke")
        print("3. Get a knock-knock joke")
        print("4. Get a general joke")
        print("5. Get a safe joke (no explicit content)")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            joke = generator.get_random_joke("Any")
            generator.display_joke(joke)
        elif choice == "2":
            joke = generator.get_random_joke("Programming")
            generator.display_joke(joke)
        elif choice == "3":
            joke = generator.get_random_joke("Knock-Knock")
            generator.display_joke(joke)
        elif choice == "4":
            joke = generator.get_random_joke("General")
            generator.display_joke(joke)
        elif choice == "5":
            joke = generator.get_random_joke_safe()
            generator.display_joke(joke)
        elif choice == "6":
            print("\nThanks for using the Joke Generator! 😄")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
