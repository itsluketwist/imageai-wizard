from enum import StrEnum


IMAGEAI_WIZARD_OPEN_AI_KEY = "IMAGEAI_WIZARD_OPEN_AI_KEY"

DEFAULT_MAX_TOKENS = 200

DEFAULT_TEMPERATURE = 0.7

DEFAULT_MODEL = "gpt-3.5-turbo"


class Persona(StrEnum):
    CHILD = "child"
    BUSINESS_PERSON = "business person"
    ACADEMIC_PROFESSOR = "academic professor"


class Tone(StrEnum):
    ANGRY = "angry"
    CHEERFUL = "cheerful"
    CONFUSED = "confused"
