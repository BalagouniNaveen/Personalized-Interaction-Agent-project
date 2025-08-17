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
