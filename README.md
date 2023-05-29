# **imageai-wizard**

ImageAI Wizard is a Python library that provides an easy-to-use interface for generating 
various data about images using the OpenAI API.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## *installation*

ImageAI Wizard can be installed via pip:

```shell
pip install git+https://github.com/itsluketwist/imageai-wizard
```

## *usage*

First, you need to obtain an API key from OpenAI (use [this](https://platform.openai.com/account/api-keys) 
interface, you must be [signed up](https://beta.openai.com/signup/)).

This key must be provided when initialising the `Wizard` class, or stored in the
`IMAGEAI_WIZARD_OPEN_AI_KEY` environment variable. The code will error if no key is provided.

```python
from imageai_wizard import Wizard, Persona, Tone

wiz = Wizard(api_key='YOUR_API_KEY')

image_url = "https://upload.wikimedia.org/wikipedia/en/thumb/4/47/Iron_Man_%28circa_2018%29.png/220px-Iron_Man_%28circa_2018%29.png"

# generate text based responses about the image
description = wiz.generate_description(
    image=image_url,
    persona=Persona.CHILD,
    tone=Tone.CHEERFUL,
)
print(f"Description: {description}")

caption = wiz.generate_caption(
    image=image_url,
    persona=Persona.ACADEMIC_PROFESSOR,
    tone=Tone.ANGRY,
)
print(f"Caption: {caption}")

title = wiz.generate_title(
    image=image_url,
    persona=Persona.BUSINESS_PERSON,
    tone=Tone.CONFUSED,
)
print(f"Title: {title}")

# generate a comparison to another image
another_image_url = "https://e0.pxfuel.com/wallpapers/971/526/desktop-wallpaper-robot-and-cat-red-robot.jpg"
comparison = wiz.compare_images(
    image_1=image_url,
    image_2=another_image_url,
)
print(f"Comparison: {comparison}")
```


## *development*

Clone the repository code:

```shell
git clone https://github.com/itsluketwist/imageai-wizard.git
```

Once cloned, install the package locally in a virtual environment:

```shell
python -m venv venv

. venv/bin/activate

pip install -e ".[dev]"
```

Install and use pre-commit to ensure code is in a good state:

```shell
pre-commit install

pre-commit run --all-files
```


## *contributing*

If you'd like to contribute to ImageAI Wizard, please fork the repository and create a pull request. 
We welcome contributions of all kinds, including bug fixes, new features, and documentation improvements.


## *license*

ImageAI Wizard is licensed under the MIT License. See [LICENSE](LICENSE) for more information.

## *inspiration*

I wanted to get more familiar with ChatGPT, it's API and writing prompts in general. 
So I did the only reasonable thing, and asked ChatGPT for a python library I could 
build that utilises the API! This was the suggestion, ChatGPT even helped me to 
write the code itself, and this readme.

Initial prompt: `Can you suggest a simple python library that I can build? the library must use your own API and be useful.`


## *todo*

- Ask ChatGPT for more ideas... and implement them, I guess?
- Add some image generation methods that utilise `openai.Image.create(...)`
