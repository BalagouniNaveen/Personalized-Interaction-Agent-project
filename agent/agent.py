from kumo.kumo_client import KumoClient

class PersonalizedAgent:
    def __init__(self):
        self.kumo = KumoClient()

    def recommend(self, user_data: dict) -> dict:
        """
        Generate a personalized recommendation for a user.
        """
        prediction = self.kumo.predict(user_data)
        # Decision logic based on engagement score
        action = prediction["recommended_action"] if prediction["engagement_score"] > 0.7 else "send_message"
        return {
            "user_id": user_data["user_id"],
            "action": action,
            "score": prediction["engagement_score"]
        }

# Test agent
if __name__ == "__main__":
    agent = PersonalizedAgent()
    test_user = {"user_id": 1, "age": 25, "gender": "M", "last_active": "2025-08-10", "interactions": 15, "purchases": 2}
    print(agent.recommend(test_user))
