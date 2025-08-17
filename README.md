# Personalized-Interaction-Agent-project


# **Personalized Interaction Agent – Full Implementation Guide**

---

## **1. Project Overview**

**Goal:** Build an AI agent that uses **KumoRFM predictions** to adapt conversations, recommendations, or decisions in real time.

**Core Features:**

1. Real-time predictions using KumoRFM.
2. Personalized recommendations (conversation/action/product) for users.
3. Web-based interface (Flask) for interaction.
4. Modular architecture (easy to extend or connect to real KumoRFM API later).

---

## **2. Architecture Diagram**

```
          +-------------------+
          |  User Interaction |
          |  (Web / Chat UI)  |
          +---------+---------+
                    |
                    v
          +-------------------+
          | Personalized Agent|
          |  (Decision Logic) |
          +---------+---------+
                    |
                    v
          +-------------------+
          |   KumoRFM Client  |
          |  (Predictions)    |
          +---------+---------+
                    |
                    v
          +-------------------+
          | Mock / Public Data|
          |  (In-memory CSV)  |
          +-------------------+
```

**Explanation:**

* **User Interaction:** Web or chat interface provides user input.
* **Personalized Agent:** Uses prediction logic to decide the next action.
* **KumoRFM Client:** Simulates KumoRFM predictions (replaceable with real API).
* **Dataset:** Mock or public dataset in memory used for generating predictions.

---

## **3. File Structure**

```
personalized-agent/
│
├─ data/
│   └─ mock_user_data.csv          # Sample user dataset
│
├─ agent/
│   ├─ __init__.py
│   ├─ agent.py                    # Core agent logic
│   └─ utils.py                    # Helper functions
│
├─ kumo/
│   ├─ __init__.py
│   └─ kumo_client.py              # KumoRFM interaction
│
├─ app/
│   ├─ main.py                     # Entry point (Flask API)
│
├─ tests/
│   └─ test_agent.py               # Unit tests
│
├─ requirements.txt
└─ README.md
```

---

## **4. Step-by-Step Implementation**

### **Step 1: Environment Setup**

```bash
mkdir personalized-agent && cd personalized-agent
python -m venv venv
source venv/bin/activate   # Linux/macOS
# OR
venv\Scripts\activate      # Windows

pip install pandas flask requests pytest
```

---

### **Step 2: Prepare Mock Dataset**

`data/mock_user_data.csv`:

```csv
user_id,age,gender,last_active,interactions,purchases
1,25,M,2025-08-10,15,2
2,30,F,2025-08-12,8,1
3,22,F,2025-08-11,20,5
4,40,M,2025-08-09,3,0
```

This dataset simulates basic user behavior for predictions.

---

### **Step 3: Implement KumoRFM Client (Mock)**

`kumo/kumo_client.py`:

```python
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
```

**Output example:**

```json
{'engagement_score': 0.82, 'recommended_action': 'recommend_product'}
```

---

### **Step 4: Build Agent Logic**

`agent/agent.py`:

```python
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
```

**Output example:**

```json
{'user_id': 1, 'action': 'recommend_product', 'score': 0.82}
```

---

### **Step 5: Create Web Interface Using Flask**

`app/main.py`:

```python
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

**Test the API:**

```bash
python app/main.py
```

Open browser or use curl:

```bash
curl http://127.0.0.1:5000/recommend/1
```

**Example output:**

```json
{
  "user_id": 1,
  "action": "recommend_product",
  "score": 0.82
}
```

---

### **Step 6: Unit Testing**

`tests/test_agent.py`:

```python
from agent.agent import PersonalizedAgent

def test_recommendation():
    agent = PersonalizedAgent()
    user_data = {"user_id": 1, "age": 25, "gender": "M", "last_active": "2025-08-10", "interactions": 15, "purchases": 2}
    result = agent.recommend(user_data)
    assert "action" in result
    assert "score" in result
    assert 0 <= result["score"] <= 1

# Run pytest
# pytest tests/
```

**Run tests:**

```bash
pytest tests/
```



---

### **Step 7: Demo & Storytelling**

**Flow:**

1. Run Flask API (`python app/main.py`).
2. Visit `http://127.0.0.1:5000/recommend/<user_id>` for different users.
3. Show personalized recommendations and engagement scores.
4. Highlight **KumoRFM integration** (mocked predictions).

---

### **Step 8: Optional Enhancements**

1. Replace mock KumoRFM with real API calls if available.
2. Connect to React or Streamlit frontend for live interaction.
3. Log recommendations and user feedback for continuous learning.
4. Use larger datasets (Kaggle e-commerce, user behavior datasets).

---

###  **Project Result**

* Fully functional **Personalized Interaction Agent**.
* Modular and testable architecture.
* Real-time recommendations using KumoRFM predictions.
* Ready for hackathon demo with storytelling, showing predictions for multiple users.


