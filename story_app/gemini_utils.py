
import google.generativeai as genai
from django.conf import settings

# Set your API key
genai.configure(api_key=settings.GEMINI_API_KEY)

# Configure the model
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to generate story parts with chaining and temperature
def generate_story(title, user_temperature=0.3):
    # Step 1: Opening
    prompt1 = f"Write a 50-word opening for a sci-fi story titled '{title}'."
    response1 = model.generate_content(prompt1, generation_config={"temperature": user_temperature})
    opening = response1.text.strip()

    # Step 2: Plot Twist
    temperature_for_twist = min(user_temperature + 0.3, 1.0)
    prompt2 = f"Continue this story: '{opening}' with a surprising plot twist, in 150 words."
    response2 = model.generate_content(prompt2, generation_config={"temperature": temperature_for_twist})
    twist = response2.text.strip()

    # Step 3: Conclusion
    full_story_so_far = opening + " " + twist
    prompt3 = f"Conclude this story: '{full_story_so_far}' in a hopeful tone, in 100 words."
    response3 = model.generate_content(prompt3, generation_config={"temperature": user_temperature})
    conclusion = response3.text.strip()

    # Combine the story parts
    full_story = f"{opening} {twist} {conclusion}"
    return full_story
