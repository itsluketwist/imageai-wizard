# imageai-wizard

[![PyPI version](https://badge.fury.io/py/imageai-wizard.svg)](https://badge.fury.io/py/imageai-wizard)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

ImageAI Wizard is a Python library that provides an easy-to-use interface for generating captions for images using the OpenAI GPT API. It also includes utility functions for resizing and downloading images.

## Installation

ImageAI Wizard can be installed via pip:

```shell
pip install imageai-wizard
```

## Usage

First, you need to obtain an API key from OpenAI [here](https://beta.openai.com/signup/). Then, you can use the library as follows:

```python
from imageai_wizard import ImageAIWizard

ai_wizard = ImageAIWizard(api_key='YOUR_API_KEY')

# Generate caption for an image file
caption = ai_wizard.generate_caption_from_file('path/to/image.jpg')

# Generate caption for an image URL
caption = ai_wizard.generate_caption_from_url('https://example.com/image.jpg')

# Resize an image
resized_image = ai_wizard.resize_image('path/to/image.jpg', new_size=(500, 500))

# Download an image from URL
ai_wizard.download_image('https://example.com/image.jpg', save_path='path/to/save/image.jpg')
```

## Contributing

If you'd like to contribute to ImageAI Wizard, please fork the repository and create a pull request. We welcome contributions of all kinds, including bug fixes, new features, and documentation improvements.

## License

ImageAI Wizard is licensed under the MIT License. See LICENSE for more information.

## Inspiration

I wanted to get more familiar with ChatGPT and it's API. So I did the only reasonable thing, and asked ChatGPT for a python library I could build that utilises the API! This was the suggestion, ChatGPT even helped me to write the code itself, and this readme.


## todo

- add features to generate / describe for word count, and for level of response (child, professor, etc)
- add initial convo image to readme
