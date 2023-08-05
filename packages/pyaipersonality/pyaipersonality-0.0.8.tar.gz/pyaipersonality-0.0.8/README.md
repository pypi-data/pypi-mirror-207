# PyAIPersonality

![GitHub license](https://img.shields.io/github/license/ParisNeo/PyAIPersonality)
![GitHub issues](https://img.shields.io/github/issues/ParisNeo/PyAIPersonality)
![GitHub stars](https://img.shields.io/github/stars/ParisNeo/PyAIPersonality)
![GitHub forks](https://img.shields.io/github/forks/ParisNeo/PyAIPersonality)
[![Discord](https://img.shields.io/discord/1092918764925882418?color=7289da&label=Discord&logo=discord&logoColor=ffffff)](https://discord.gg/4rR282WJb6)
[![Follow me on Twitter](https://img.shields.io/twitter/follow/SpaceNerduino?style=social)](https://twitter.com/SpaceNerduino)
[![Follow Me on YouTube](https://img.shields.io/badge/Follow%20Me%20on-YouTube-red?style=flat&logo=youtube)](https://www.youtube.com/user/Parisneo)

[![PyPI](https://img.shields.io/pypi/v/pyaipersonality.svg)](https://pypi.org/project/pyaipersonality/)

## Current version : 0.0.6 (GLaDOS)
## Main developer [ParisNeo](https://github.com/ParisNeo)

PyAIPersonality is a Python library for defining AI personalities for AI-based models. With PyAIPersonality, you can define a file format, assets, and personalized scripts to create unique AI personalities.

## Installation

You can install PyAIPersonality using pip:
```bash
pip install pyaipersonality
```

## Usage

Here's an example of how to use PyAIPersonality to load an AI personality and print its attributes:

```python
from pyaipersonality import AIPersonality

if __name__=="__main__":
    personality = AIPersonality("personalities_zoo/english/generic/gpt4all")
    print("Done")
    print(f"{personality}")
```

You can use PyAIPersonality with pyllamacpp python bindings by first installing pyllamacpp:
```bash
pip install pyllamacpp
```

Download one of the compatible models. Some models are better than others in simulating the personalities, so please make sure you select the right model as some models are very sparsely trained and have no enough culture to imersonate the character.

Here is a list of compatible models:
- [Main gpt4all model](https://huggingface.co/ParisNeo/GPT4All/resolve/main/gpt4all-lora-quantized-ggml.bin)
- [Main gpt4all model (unfiltered version)](https://huggingface.co/ParisNeo/GPT4All/resolve/main/gpt4all-lora-unfiltered-quantized.new.bin)
- [Vicuna 7B vrev1](https://huggingface.co/eachadea/legacy-ggml-vicuna-7b-4bit/resolve/main/ggml-vicuna-7b-4bit-rev1.bin)
- [Vicuna 13B vrev1](https://huggingface.co/eachadea/ggml-vicuna-13b-4bit/resolve/main/ggml-vicuna-13b-4bit-rev1.bin)

- [GPT-J v1.3-groovy](https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin)
- [GPT-J v1.2-jazzy](https://gpt4all.io/models/ggml-gpt4all-j-v1.2-jazzy.bin)
- [GPT-J gpt4all-j original](https://gpt4all.io/models/ggml-gpt4all-j.bin)
- [Vicuna 7b quantized v1.1 q4_2](https://gpt4all.io/models/ggml-vicuna-7b-1.1-q4_2.bin)
- [Vicuna 13b quantized v1.1 q4_2](https://gpt4all.io/models/ggml-vicuna-13b-1.1-q4_2.bin)

Then you can use this code to have an interactive communication with the AI through the console :
```python
from pyaipersonality import AIPersonality
from pyllamacpp.model import Model

from pathlib import Path
import urllib.request
import sys
import os

from tqdm import tqdm

# You need to install pyllamacpp from pypi:
# pip install pyllamacpp

if __name__=="__main__":

    # choose your model
    # undomment the model you want to use
    # These models can be automatically downloaded
    # url = "https://huggingface.co/ParisNeo/GPT4All/resolve/main/gpt4all-lora-quantized-ggml.bin"
    # url = "https://huggingface.co/ParisNeo/GPT4All/resolve/main/gpt4all-lora-unfiltered-quantized.new.bin"
    # url = "https://huggingface.co/eachadea/legacy-ggml-vicuna-7b-4bit/resolve/main/ggml-vicuna-7b-4bit-rev1.bin"
    url = "https://huggingface.co/eachadea/ggml-vicuna-13b-4bit/resolve/main/ggml-vicuna-13b-4bit-rev1.bin"
    # You can add any llamacpp compatible model

    model_name  = url.split("/")[-1]
    folder_path = Path("models/")

    model_full_path = (folder_path / model_name)

    # Check if file already exists in folder
    if model_full_path.exists():
        print("File already exists in folder")
    else:
        # Create folder if it doesn't exist
        folder_path.mkdir(parents=True, exist_ok=True)
        progress_bar = tqdm(total=None, unit="B", unit_scale=True, desc=f"Downloading {url.split('/')[-1]}")
        # Define callback function for urlretrieve
        def report_progress(block_num, block_size, total_size):
            progress_bar.total=total_size
            progress_bar.update(block_size)
        # Download file from URL to folder
        try:
            urllib.request.urlretrieve(url, folder_path / url.split("/")[-1], reporthook=report_progress)
            print("File downloaded successfully!")
        except Exception as e:
            print("Error downloading file:", e)
            sys.exit(1)

    personality = AIPersonality("personalities_zoo/english/generic/gpt4all")
    full_context = personality.personality_conditioning+personality.link_text+personality.ai_message_prefix+personality.welcome_message if personality.welcome_message!="" else personality.personality_conditioning
    model = Model(model_path=f'models/{url.split("/")[-1]}',
                  prompt_context=full_context,
                  prompt_prefix=personality.link_text + personality.user_message_prefix + personality.link_text,
                  prompt_suffix=personality.link_text + personality.ai_message_prefix + personality.link_text
                  )
    # If there is a disclaimer, show it
    if personality.disclaimer!="":
        print()
        print("Disclaimer")
        print(personality.disclaimer)
        print()

    # Show conditionning
    print(full_context)
    
    while True:
        try:
            prompt = input("You: ")
            if prompt == '':
                continue
            print(f"{personality.name}:", end='')
            output=""
            for tok in model.generate(
                            prompt, 
                            n_predict=personality.model_n_predicts, 
                            temp=personality.model_temperature,
                            top_k=personality.model_top_k,
                            top_p=personality.model_top_p,
                            repeat_last_n=personality.model_repeat_last_n,
                            repeat_penalty=personality.model_repeat_penalty
                        ):
                output += tok

                # Use Hallucination suppression system
                if personality.detect_antiprompt(output):
                    break
                else:
                    print(f"{tok}", end='', flush=True)
            print()
        except KeyboardInterrupt:
            print("Keyboard interrupt detected.\nBye")
            break
    print("Done")
    print(f"{personality}")
```

# Naming Rationale
For our new multi-personality AI agent library, we wanted to come up with a naming scheme that reflected our love for science fiction and artificial intelligence. Each release of the application will feature a different AI agent with a distinct personality and set of capabilities, so we felt it was important to give each version a unique and memorable name.

# Current version name: GLaDOS
GLaDOS is a fictional AI character from the popular video game series "Portal" developed by Valve Corporation. She serves as the primary antagonist throughout the series, with her primary function being the management of the Aperture Science Enrichment Center.

GLaDOS, which stands for "Genetic Lifeform and Disk Operating System," is designed as a highly intelligent and manipulative AI. She speaks in a calm and monotone voice, often using sarcastic humor and passive-aggressive language to communicate with the player character, Chell.

Throughout the series, GLaDOS is depicted as being both ruthless and resourceful, often using deadly force and deception to achieve her goals. Despite her malicious behavior, she is also shown to have a complex and troubled history, with much of her backstory revealed over the course of the games.

Overall, GLaDOS is a memorable and iconic AI character in sci-fi culture, known for her wit, sarcasm, and unpredictable behavior.

# Contributing
Contributions to PyAIPersonality are welcome! If you'd like to contribute, please follow these steps:

1. Fork this repository
2. Create a new branch (`git checkout -b my-new-branch`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin my-new-branch`)
6. Create a new pull request


# License
PyAIPersonality is licensed under the Apache 2.0 license. See the `LICENSE` file for more information.
