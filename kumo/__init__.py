

"""
This file marks the 'kumo' directory as a Python package
and exposes key classes for easy imports.

Usage:
    from kumo import KumoClient
"""

from .kumo_client import KumoClient

# Define what is publicly accessible when importing the package
__all__ = ["KumoClient"]
