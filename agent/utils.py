import datetime

def validate_user_data(user_data: dict) -> bool:
    """
    Validates that the user data has all required fields.
    Returns True if valid, False otherwise.
    """
    required_fields = ["user_id", "age", "gender", "last_active", "interactions", "purchases"]
    for field in required_fields:
        if field not in user_data:
            return False
    return True


def parse_date(date_str: str) -> datetime.date:
    """
    Converts a string (YYYY-MM-DD) to a datetime.date object.
    """
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}, expected YYYY-MM-DD")


def days_since_last_active(last_active_date: str) -> int:
    """
    Returns the number of days since the user was last active.
    """
    last_active = parse_date(last_active_date)
    today = datetime.date.today()
    delta = today - last_active
    return delta.days


def format_recommendation_output(user_id: int, action: str, score: float) -> dict:
    """
    Formats the recommendation output consistently for API response.
    """
    return {
        "user_id": user_id,
        "action": action,
        "engagement_score": round(score, 2)
    }
