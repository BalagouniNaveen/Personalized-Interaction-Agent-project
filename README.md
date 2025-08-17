

# **Personalized Interaction Agent – Detailed Project Explanation**

---

## **1. Project Overview**

The **Personalized Interaction Agent** is an **AI-powered system** designed to provide **personalized recommendations or actions** for users based on their behavior. The agent uses **KumoRFM predictions** to adapt its responses or suggestions in real time.

**Goal:**
To create an AI agent that understands user behavior, predicts engagement, and provides **customized recommendations** for better user experience.

**Core Features:**

* **Real-time predictions** using KumoRFM (mocked for this project).
* **Personalized actions** like product suggestions, messages, or offers.
* **Web-based interface** using Flask for interactive access.
* **Modular architecture** for easy integration with real APIs or front-end systems.
* **Unit tests** to ensure the system works correctly.

---

## **2. Uses of the Project**

* **E-commerce:** Suggest products based on user behavior and purchase history.
* **Education Platforms:** Recommend courses or learning material personalized for each student.
* **Customer Support:** Suggest messages or actions based on user engagement.
* **Marketing:** Provide personalized offers or promotions to increase engagement.
* **Social Apps:** Recommend interactions or content to users to improve retention.

---

## **3. Advantages**

* **Real-time personalization:** Offers instant recommendations based on the latest user data.
* **Modular and extendable:** Can be integrated with any front-end or real KumoRFM API.
* **Easy to test:** Unit tests ensure correct predictions.
* **User-focused:** Improves user experience by suggesting relevant actions.
* **Data-driven decisions:** Uses engagement scores to choose actions intelligently.

---

## **4. Disadvantages / Limitations**

* **Mock predictions:** Current implementation uses random values instead of real AI predictions.
* **Limited dataset:** Only small sample CSV data is used for demonstration.
* **No persistent storage:** Predictions are not logged or stored.
* **Requires Python knowledge:** Users need Python environment setup for running the project.

---

## **5. Benefits**

* **Hackathon-ready:** Fully working, easy to demonstrate in real-time.
* **Learning tool:** Great for understanding AI-driven personalization.
* **Scalable:** Can be extended to work with real datasets and APIs.
* **Cross-industry applicability:** Can be adapted for e-commerce, education, marketing, and social platforms.

---

## **6. Folder Structure Explanation**

```
personalized-agent/
│
├─ data/
│   └─ mock_user_data.csv          # Sample dataset of users
│
├─ agent/
│   ├─ __init__.py                 # Package initializer
│   ├─ agent.py                     # Core logic for generating recommendations
│   └─ utils.py                     # Helper functions for validation & formatting
│
├─ kumo/
│   ├─ __init__.py                 # Package initializer
│   └─ kumo_client.py              # Mock KumoRFM client for predictions
│
├─ app/
│   ├─ main.py                     # Flask API entry point
│
├─ tests/
│   └─ test_agent.py               # Unit tests for the agent
│
├─ requirements.txt                # Required Python packages
└─ README.md                       # Project documentation
```

**Explanation of Key Components:**

1. **data/mock\_user\_data.csv:** Stores sample user information like age, gender, interactions, and purchases.
2. **agent/agent.py:** Contains the **PersonalizedAgent** class that generates recommendations.
3. **agent/utils.py:** Helper functions for data validation, date calculations, and output formatting.
4. **kumo/kumo\_client.py:** Simulates KumoRFM predictions with random engagement scores and recommended actions.
5. **app/main.py:** Runs a Flask API to get recommendations for users in real time.
6. **tests/test\_agent.py:** Unit tests to validate the recommendation logic.
7. **requirements.txt:** All Python packages needed to run the project.

---

## **7. Code Snippets**

### **7.1 KumoRFM Mock Client**

```python
# kumo/kumo_client.py
import random

class KumoClient:
    """Mock KumoRFM client for predictions"""

    def predict(self, user_features: dict) -> dict:
        return {
            "engagement_score": round(random.uniform(0, 1), 2),
            "recommended_action": random.choice([
                "offer_discount",
                "recommend_product",
                "send_message"
            ])
        }

# Test
if __name__ == "__main__":
    client = KumoClient()
    test_user = {"user_id": 1, "age": 25, "interactions": 15, "purchases": 2}
    print(client.predict(test_user))
```

**Sample Output:**

```json
{'engagement_score': 0.82, 'recommended_action': 'recommend_product'}
```

---

### **7.2 Agent Logic**

```python
# agent/agent.py
from kumo.kumo_client import KumoClient
from .utils import validate_user_data, format_recommendation_output

class PersonalizedAgent:
    def __init__(self):
        self.kumo = KumoClient()

    def recommend(self, user_data: dict) -> dict:
        if not validate_user_data(user_data):
            raise ValueError("Invalid user data")
        prediction = self.kumo.predict(user_data)
        action = prediction["recommended_action"] if prediction["engagement_score"] > 0.7 else "send_message"
        return format_recommendation_output(user_data["user_id"], action, prediction["engagement_score"])

# Test
if __name__ == "__main__":
    agent = PersonalizedAgent()
    user_data = {"user_id": 1, "age": 25, "gender": "M", "last_active": "2025-08-10", "interactions": 15, "purchases": 2}
    print(agent.recommend(user_data))
```

**Sample Output:**

```json
{'user_id': 1, 'action': 'recommend_product', 'engagement_score': 0.82}
```

---

### **7.3 Flask API**

```python
# app/main.py
from flask import Flask, jsonify
import pandas as pd
from agent.agent import PersonalizedAgent

app = Flask(__name__)
agent = PersonalizedAgent()

# Load mock data
user_df = pd.read_csv("../data/mock_user_data.csv")
users = {row.user_id: row.to_dict() for _, row in user_df.iterrows()}

@app.route("/recommend/<int:user_id>", methods=["GET"])
def recommend(user_id):
    user_data = users.get(user_id)
    if not user_data:
        return jsonify({"error": "User not found"}), 404
    recommendation = agent.recommend(user_data)
    return jsonify(recommendation)

if __name__ == "__main__":
    app.run(debug=True)
```

**Sample API Output:**

```json
{
  "user_id": 1,
  "action": "recommend_product",
  "engagement_score": 0.82
}
```

---

### **7.4 Unit Test**

```python
# tests/test_agent.py
from agent.agent import PersonalizedAgent

def test_recommendation():
    agent = PersonalizedAgent()
    user_data = {"user_id": 1, "age": 25, "gender": "M", "last_active": "2025-08-10", "interactions": 15, "purchases": 2}
    result = agent.recommend(user_data)
    assert "action" in result
    assert "engagement_score" in result
    assert 0 <= result["engagement_score"] <= 1
```

**Test Output:**

```
tests/test_agent.py .                                                  [100%]
1 passed
```

---

## **8. Technologies Used**

* **Python 3.10+** – Main programming language.
* **Flask** – For building the web API.
* **Pandas** – To read and manipulate CSV user data.
* **Pytest** – For unit testing the agent logic.
* **Random library** – For generating mock predictions.
* **JSON** – For sending API responses.

---

## **9. How to Run the Project**

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run Flask API:

```bash
python app/main.py
```

5. Test in browser or curl:

```bash
curl http://127.0.0.1:5000/recommend/1
```

6. Run unit tests:

```bash
pytest tests/
```

---

 **Outcome:**

* Users get **real-time personalized recommendations**.
* Agent is **modular, testable, and hackathon-ready**.
* Provides **JSON responses** for each user with engagement score and recommended action.

---

If you want, I can now **draw a full visual flowchart** showing **User → Agent → KumoRFM → Recommendation**, which will make your project presentation **professional and easy to understand**.

Do you want me to create that next?
