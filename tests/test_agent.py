from agent.agent import PersonalizedAgent

def test_recommendation():
    agent = PersonalizedAgent()
    user_data = {
        "user_id": 1,
        "age": 25,
        "gender": "M",
        "last_active": "2025-08-10",
        "interactions": 15,
        "purchases": 2
    }
    result = agent.recommend(user_data)
    assert "action" in result
    assert "score" in result
    assert 0 <= result["score"] <= 1
