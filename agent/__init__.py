"""
This file marks the 'agent' directory as a Python package
and exposes key classes and functions for easy imports.

Usage:
    from agent import PersonalizedAgent
    from agent import validate_user_data, days_since_last_active, format_recommendation_output
"""

from .agent import PersonalizedAgent
from .utils import validate_user_data, days_since_last_active, format_recommendation_output

# Define what is publicly accessible when importing the package
__all__ = [
    "PersonalizedAgent",
    "validate_user_data",
    "days_since_last_active",
    "format_recommendation_output"
]
