"""Compute a simple inner product and print the cosine of two vectors.

The script answers: given two vectors in R^2, what scalar does the standard
inner product assign, and how does that relate to the angle between them?
"""

from __future__ import annotations

import numpy as np


def cosine_similarity(u: np.ndarray, v: np.ndarray) -> float:
    """Return the cosine of the angle between ``u`` and ``v``.

    Args:
        u: First vector, shape ``(d,)``.
        v: Second vector, shape ``(d,)``.

    Returns:
        Cosine of the angle. The value is in ``[-1, 1]`` when both vectors
        are nonzero.

    Raises:
        ValueError: If either vector is the zero vector.
    """
    u_norm = np.linalg.norm(u)
    v_norm = np.linalg.norm(v)
    if u_norm == 0.0 or v_norm == 0.0:
        raise ValueError("cosine similarity is undefined for a zero vector")
    return float(np.dot(u, v) / (u_norm * v_norm))


def main() -> None:
    """Run the inner-product example with a fixed pair of vectors."""
    u = np.array([2.4, 1.5])
    v = np.array([2.1, 0.0])
    print(f"u · v = {np.dot(u, v):.4f}")
    print(f"cos(theta) = {cosine_similarity(u, v):.4f}")


if __name__ == "__main__":
    main()
