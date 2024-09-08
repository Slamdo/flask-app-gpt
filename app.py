# from openai import OpenAI
import os

import openai
import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, request

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)


# Route to analyze sentiment using OpenAI GPT
@app.route("/sentiment", methods=["POST"])
def analyze_sentiment():
    try:
        # Extract the OpenAI API key and the text to analyze from the POST request

        text = request.json.get("text")

        # Set the OpenAI API key
        # openai.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = "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" # api key

        # Make a request to the OpenAI GPT-3.5 API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {
                    "role": "system",
                    # prompt
                    "content": "บอกคำของศัพท์แสลงภาษาอังกฤษ บอกเป็นภาษาไทย แยกเป็นคำ::",
                },
                {"role": "user", "content": text},
            ],
        )

        # Extract the sentiment from the response
        sum_response = response["choices"][0]["message"]["content"].strip()


        return jsonify({"summary": sum_response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
