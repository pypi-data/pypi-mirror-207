"""PYTZEN

version: 0.0.112
"""

from .ai_joke_generator import AIJokeGenerator

joke_generator = AIJokeGenerator()
print(joke_generator.get_joke())