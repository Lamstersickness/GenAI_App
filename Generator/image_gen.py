from openai import OpenAI
from PIL import Image
import requests
from io import BytesIO
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_image_from_text(prompt):
    try:
        response = client.images.generate(
            model="dall-e-3",  
            prompt=prompt,
            size="1024x1024",  
            quality="standard",
            n=1
        )
        image_url = response.data[0].url
        image_response = requests.get(image_url)
        image = Image.open(BytesIO(image_response.content))
        return image
    except Exception as e:
        return f"Error generating image: {e}"
