from flask import Flask, render_template, request
import google.generativeai as genai
import os

app = Flask(__name__)

# ✅ Configure your API key here
genai.configure(api_key="AIzaSyBVNDhsLeibT00_1TvhuBVjTuZrQIr-XU8")

# ✅ Use correct model name
model = genai.GenerativeModel("gemini-2.0-flash")

@app.route("/", methods=["GET", "POST"])
def home():
    recipe = None
    if request.method == "POST":
        ingredients = request.form["ingredients"]
        prompt = f"Create a delicious recipe using these ingredients: {ingredients}"
        
        try:
            response = model.generate_content(prompt)
            recipe = response.text.strip()
        except Exception as e:
            recipe = f"⚠️ Error generating recipe: {e}"

    return render_template("index.html", recipe=recipe)

if __name__ == "__main__":
    app.run(debug=True)
