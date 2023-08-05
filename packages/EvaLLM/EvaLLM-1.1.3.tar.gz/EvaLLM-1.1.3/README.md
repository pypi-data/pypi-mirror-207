
## EvaLLM
A Python Package that incorporates emotional AI into your code.

## Getting Started
Getting started is incredibly simple. First, install EvaLLM by using pip.
    `pip install evallm`
The modules will not install yet, as they install when you first run.

## Usage
Now that you've installed, you can use the `respond()` function. There is 1 required parameter, and 1 optional. Prompt is the prompt for Eva. Temperature is a decimal integer between 0 and 1 that determines how creative Eva will be. If you have worked with GPT-3, then it works the same here. An example usage of a chat application with Eva may look like this:

```
#Import packages
import evallm as eva

# Start a conversation
while True:
    # Get user input
    user_input = input("You: ")

    # Get Eva's response
    response = eva.respond(user_input)

    # Print Eva's response
    print("Eva:", response)
```
This results in a conversation like this:
```
You: Hi! How are you doing?
Eva: I'm doing alright, thank you. How about you?
You: Good, thanks for asking!
Eva: You're welcome, I'm happy to be informed. (＾▽＾)
```

## Mascot
Eva has an official mascot. It is a female girl, often depicted in the style of Anime. Here's a picture:
![Image of Eva](https://codesoft-assets.codesoftgames.repl.co/eva/transparent.png)