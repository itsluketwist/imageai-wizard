import requests
import openai
import base64
from io import BytesIO
from PIL import Image

openai.api_key = "YOUR_API_KEY"

class ImageAIWizard:
    """
    A class for performing various AI-based image tasks using OpenAI's GPT-3 API.
    """
    
    def __init__(self, api_key: str, model_engine: str = "text-davinci-002") -> None:
        """
        Constructor for the ImageAIWizard class.
        
        Parameters:
            api_key (str): Your OpenAI API key.
            model_engine (str): The GPT-3 model engine to use. Defaults to "text-davinci-002".
        """
        openai.api_key = api_key
        self.model_engine = model_engine

    def compare_images(self, image1_url: str, image2_url: str) -> float:
        """
        Compares two images and returns a score indicating their similarity.

        todo: use this in the prompt:
        "Please give your response in the following json format: 
        {"score": 0.5, "description": "Some description of the similarities and differences"}
        Only provide the json, nothing else in the response."
        
        Parameters:
            image1_url (str): The URL of the first image.
            image2_url (str): The URL of the second image.
            
        Returns:
            float: A score indicating the similarity between the two images.
        """
        image1 = self._get_image_from_url(image1_url)
        image2 = self._get_image_from_url(image2_url)
        prompt = f"Compare these two images and give a score from 0 to 1 on how similar they are:\n\nImage 1:\n{image1}\n\nImage 2:\n{image2}\n\nScore:"

        response = self._get_openai_response(prompt)
        return float(response['choices'][0]['text'].strip())

    def generate_image(self, prompt: str, image_width: int = 512, image_height: int = 512) -> Image:
        """
        Generates an image based on a prompt using the GPT-3 API.
        
        Parameters:
            prompt (str): The prompt to use for generating the image.
            image_width (int): The desired width of the generated image in pixels. Defaults to 512.
            image_height (int): The desired height of the generated image in pixels. Defaults to 512.
            
        Returns:
            Image: A PIL Image object containing the generated image.
        """
        response = self._get_openai_response(prompt)
        image_data = response['choices'][0]['text']
        image_bytes = base64.b64decode(image_data)
        image = Image.open(BytesIO(image_bytes))
        image = self._resize_image(image, image_width, image_height)
        return image

    # def generate_description(self, image_url: str) -> str:
    #     """
    #     Generates a textual description of an image using the GPT-3 API.
        
    #     Parameters:
    #         image_url (str): The URL of the image to describe.
            
    #     Returns:
    #         str: A textual description of the image.
    #     """
    #     image = self._get_image_from_url(image_url)
    #     prompt = f"Describe this image:\n\n{image}\n\nDescription:"
    #     response = self._get_openai_response(prompt)
    #     return response['choices'][0]['text'].strip()

    # def _get_image_from_url(self, image_url: str) -> str:
    #     """
    #     Retrieves an image from a URL and returns a string representation of it
    #     that can be used as input to the GPT-3 API.
        
    #     Parameters:
    #         image_url (str): The URL of the image to retrieve.
            
    #     Returns:
    #         str: A string representation of the image.
    #     """
    #     response =

    def generate_description(self, image_url: str) -> str:
        """
        Generates a description of an image using the OpenAI GPT API.

        Args:
            image_url: The URL of the image to describe.

        Returns:
            A string containing the description of the image.
        """
        # response = requests.get(image_url)
        # image = BytesIO(response.content).read()

        prompt = f"Describe this image: {image_url}\n"

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7,
        )
        print(response)
        description = response.choices[0].text.strip()
        return description

    def generate_caption(self, image_url: str) -> str:
        """
        Generates a caption for an image using the OpenAI GPT API.

        Args:
            image_url: The URL of the image to caption.

        Returns:
            A string containing the caption for the image.
        """
        # response = requests.get(image_url)
        # image = BytesIO(response.content).read()

        prompt = f"Caption this image: {image_url}\n"

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7,
        )
        print(response)
        caption = response.choices[0].text.strip()
        return caption

