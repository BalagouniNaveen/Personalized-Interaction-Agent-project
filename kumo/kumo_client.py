import random

class KumoClient:
    """
    Mock KumoRFM client to simulate predictions.
    """

    def predict(self, user_features: dict) -> dict:
        """
        Returns a prediction for engagement score and recommended action.
        """
        return {
            "engagement_score": round(random.uniform(0, 1), 2),
            "recommended_action": random.choice([
                "offer_discount",
                "recommend_product",
                "send_message"
            ])
        }

# Test snippet
if __name__ == "__main__":
    kumo = KumoClient()
    test_user = {"user_id": 1, "age": 25, "interactions": 15, "purchases": 2}
    print(kumo.predict(test_user))
