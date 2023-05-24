from typing import NamedTuple


class ImageAnalysis(NamedTuple):
    """
    A simple return type for image analysis data that contains
    both a numbered score along with a textual response.
    """

    score: int
    reason: str
