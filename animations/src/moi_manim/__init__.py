"""Manim helpers aligned with the book light and dark editions.

This package is a small animation library, not a scene dump. Scene scripts
live under ``animations/scenes/`` and import colours and helpers from here.
"""

from moi_manim.theme import DARK, LIGHT, BookTheme, theme_from_name

__all__ = ["DARK", "LIGHT", "BookTheme", "theme_from_name"]
