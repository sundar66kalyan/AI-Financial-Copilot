from google import genai
from google.genai.errors import ServerError
from backend.app.core.config import settings

client = genai.Client(api_key=settings.GOOGLE_API_KEY)


def generate_response(prompt: str) -> str:
    """
    Generate a response using Gemini.
    """

    try:
        response = client.models.generate_content(
            model="models/gemini-3.5-flash-lite",
            contents=prompt,
        )

        return response.text

    except ServerError:
        return (
            "Gemini service is temporarily busy. "
            "Please try again in a few seconds."
        )

    except Exception as e:
        return f"Gemini Error: {str(e)}"