import json
import os
from typing import Optional, Union

import openai

from .constants import (
    DEFAULT_MAX_TOKENS,
    DEFAULT_MODEL,
    DEFAULT_TEMPERATURE,
    IMAGEAI_WIZARD_OPEN_AI_KEY,
    Persona,
    Tone,
)
from .types import ImageAnalysis


class Wizard:
    """
    A class for performing various AI-based image tasks using OpenAI\"s API.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = DEFAULT_MODEL,
        max_tokens: int = DEFAULT_MAX_TOKENS,
        temperature: float = DEFAULT_TEMPERATURE,
    ) -> None:
        """
        Constructor for the ImageAIWizard class.

        Parameters
        ----------
        api_key : Optional[str]
            Your OpenAI API key, if `None`, the `IMAGEAI_WIZARD_OPEN_AI_KEY` environment
            variable will be used.
        model : str
            Which OpenAI text model engine to use.
        max_tokens : int
            The maximum tokens to request when generating a text response from the API.
        temperature : int
            What sampling temperature to use when querying the API, between 0 and 2.
        """
        self.api_key = api_key or os.getenv(IMAGEAI_WIZARD_OPEN_AI_KEY, None)

        if self.api_key is None:
            raise ValueError("A valid OpenAI API key is required.")

        openai.api_key = api_key

        self._model = model
        self._max_tokens = max_tokens

        if temperature < 0:
            self._temperature = 0.0
        elif temperature > 2:
            self._temperature = 2.0
        else:
            self._temperature = temperature

    def _text_generation_prompt(
        self,
        initial_prompt: str,
        length: int,
        persona: Union[Persona, str, None],
        tone: Union[Tone, str, None],
    ) -> str:
        """
        Complete a text generation prompt, using the given options.

        Parameters
        ----------
        initial_prompt : str
            The starting point for the text generation.
        length : int
            Approximate length of the response.
        persona : Union[Persona, str, None]
            What persona should be considered when giving the response.
        tone: Union[Tone, str, None]
            What tone of voice should be used in the response.

        Returns
        -------
        str
            The generated prompt response.
        """

        prompt = (
            initial_prompt + f"\nKeep your response to under {length} words long.\n"
        )

        if persona is not None:
            prompt += f'Describe the image as if you"re a {persona}.\n'

        if tone is not None:
            prompt += f"Use a {persona} tone of voice.\n"

        response = openai.Completion.create(
            prompt=prompt,
            engine=self._model,
            temperature=self._temperature,
            max_tokens=self._max_tokens,
            n=1,
        )
        response = response.choices[0].text.strip()
        return response

    def generate_description(
        self,
        image_url: str,
        length: int = 50,
        persona: Union[Persona, str, None] = None,
        tone: Union[Tone, str, None] = None,
    ) -> str:
        """
        Generates a detailed description for any given image.

        Parameters
        ----------
        image_url : str
            The url of the image.
        length : int
            Approximate length of the response.
        persona : Union[Persona, str, None]
            What persona should be considered when giving the response.
        tone: Union[Tone, str, None]
            What tone of voice should be used in the response.

        Returns
        -------
        str
            A detailed description of the image.
        """
        prompt = f"Provide a detailed description for this image: {image_url}"

        return self._text_generation_prompt(
            initial_prompt=prompt,
            persona=persona,
            tone=tone,
            length=length,
        )

    def generate_caption(
        self,
        image_url: str,
        length=20,
        persona: Union[Persona, str, None] = None,
        tone: Union[Tone, str, None] = None,
    ) -> str:
        """
        Generates an interesting caption for any given image.

        Parameters
        ----------
        image_url : str
            The url of the image.
        length : int
            Approximate length of the response.
        persona : Union[Persona, str, None]
            What persona should be considered when giving the response.
        tone: Union[Tone, str, None]
            What tone of voice should be used in the response.

        Returns
        -------
        str
            An interesting caption for the image.
        """
        prompt = f"Provide a short, interesting and catchy caption for this image: {image_url}"

        return self._text_generation_prompt(
            initial_prompt=prompt,
            persona=persona,
            tone=tone,
            length=length,
        )

    def generate_title(
        self,
        image_url: str,
        length=10,
        persona: Union[Persona, str, None] = None,
        tone: Union[Tone, str, None] = None,
    ) -> str:
        """
        Generates a captivating title for any given image.

        Parameters
        ----------
        image_url : str
            The url of the image.
        length : int
            Approximate length of the response.
        persona : Union[Persona, str, None]
            What persona should be considered when giving the response.
        tone: Union[Tone, str, None]
            What tone of voice should be used in the response.

        Returns
        -------
        str
            A gripping title for the image.
        """
        prompt = (
            f"Provide a short, catchy title for a news article that uses the following image, "
            f"it must be grab the readers attention, so be creative: {image_url}"
        )

        return self._text_generation_prompt(
            initial_prompt=prompt,
            persona=persona,
            tone=tone,
            length=length,
        )

    def compare_images(
        self,
        image_url_1: str,
        image_url_2: str,
    ) -> ImageAnalysis:
        """
        Compares two images and returns a score indicating their similarity.

        Parameters
        ----------
        image_url_1 : str
        image_url_2 : str
            The urls of the two images that should be compared.

        Returns
        -------
        ImageAnalysis
            A tuple containing both a similarity score between 0 and 100, and an
            explanation of the similarities and differences.
        """
        prompt = (
            f"Compare these two images and give an integer score from 0 to 100 "
            f"inclusive on how similar they are, along with an explanation.\n"
            f"Give your response in the following json format:\n"
            f"{{"
            f' "score": your integer score, '
            f' "explanation": "Some explanation of the similarities and differences."'
            f"}}\n"
            f"Only provide the json and nothing else in the response."
            f":\nImage 1: {image_url_1}\nImage 2: {image_url_2}\n"
        )

        response = openai.Completion.create(
            prompt=prompt,
            engine=self._model,
            temperature=self._temperature,
            max_tokens=self._max_tokens,
            n=1,
        )
        response = response.choices[0].text.strip()

        json_resp = json.loads(response)
        return ImageAnalysis(*json_resp.values())
