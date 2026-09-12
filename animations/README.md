# Animations

Manim library and scenes for *Mathematics of Intelligence*.

Scenes are grouped by the two intellectual threads, not by chapter number:

```text
animations/
├── src/moi_manim/     # reusable colours and helpers
└── scenes/
    ├── mathematics/
    ├── ai/
    └── topics/        # finance, physics, …
```

Rendered media is written to `media/` and is gitignored.

## Setup

```bash
cd animations
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -e .
```

## Render

```bash
manim -pql scenes/mathematics/example.py ExampleScene
```

Use `moi_manim.LIGHT` or `moi_manim.DARK` so films match the book editions.
