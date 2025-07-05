import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")

class MistralAIClient:
    def __init__(self):
        if not MISTRAL_API_KEY:
            print("Warning: MISTRAL_API_KEY environment variable is not set. Mistral AI features will be disabled.")
            self.client = None
        else:
            self.client = MistralClient(api_key=MISTRAL_API_KEY)

    def generate_text(self, prompt, model="mistral-tiny"):
        if self.client:
            try:
                messages = [ChatMessage(role="user", content=prompt)]
                chat_response = self.client.chat(model=model, messages=messages)
                return chat_response.choices[0].message.content
            except Exception as e:
                print(f"Error generating text with Mistral AI: {e}")
                return None
        else:
            print("Mistral AI client not initialized. Text generation disabled.")
            return None

    # You can add more methods here for other Mistral AI functionalities like embeddings, etc.

# Example usage (for testing purposes)
# if __name__ == "__main__":
#     # export MISTRAL_API_KEY="your_mistral_api_key"
#     mistral_client = MistralAIClient()
#     response = mistral_client.generate_text("Explain options arbitrage in simple terms.")
#     if response:
#         print("Mistral AI Response:", response)


