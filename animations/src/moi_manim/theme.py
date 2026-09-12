"""Colour tokens that match the LaTeX light and dark page themes.

The hex values follow ``book/preamble/theme-light.tex`` and
``book/preamble/theme-dark.tex`` so rendered films sit next to the PDF
without a second palette.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BookTheme:
    """A named palette for Manim scenes that follow the book editions.

    Attributes:
        name: Either ``light`` or ``dark``.
        page: Page or frame background.
        ink: Primary mark colour (text, axes, default strokes).
        muted: Secondary marks and labels.
        accent: Emphasis colour used for the object under discussion.
    """

    name: str
    page: str
    ink: str
    muted: str
    accent: str


LIGHT = BookTheme(
    name="light",
    page="#F7F4EE",
    ink="#1C1915",
    muted="#5C564C",
    accent="#8A4B2F",
)

DARK = BookTheme(
    name="dark",
    page="#12141A",
    ink="#E8E6E1",
    muted="#A8A39A",
    accent="#D4A27F",
)


def theme_from_name(name: str) -> BookTheme:
    """Return the book theme for ``light`` or ``dark``.

    Args:
        name: Theme identifier. Comparison is case-insensitive.

    Returns:
        The matching :class:`BookTheme`.

    Raises:
        ValueError: If ``name`` is not ``light`` or ``dark``.
    """
    key = name.strip().lower()
    if key == "light":
        return LIGHT
    if key == "dark":
        return DARK
    raise ValueError(f"Unknown theme {name!r}; expected 'light' or 'dark'.")
