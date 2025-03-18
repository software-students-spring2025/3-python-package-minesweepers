# Discordify

[![CI / CD](https://github.com/software-students-spring2025/3-python-package-minesweepers/actions/workflows/build.yaml/badge.svg)](https://github.com/software-students-spring2025/3-python-package-minesweepers/actions/workflows/build.yaml)

A Python package that transforms your text into various Discord-inspired chat styles! Perfect for adding personality to your messages or just having fun with text transformation.

## Team Members

- [Harini Buddaluru](https://github.com/peanutoil)
- [Franyel Diaz Rodriguez](https://github.com/Franyel1)
- [Suhan]
- [Jackson Chen](https://github.com/jaxxjj)
## Installation

You can install Discordify directly from [PyPI]():

```bash
pip install discordify
```

## Features

Discordify offers five different text transformation functions:

### 1. Stutterify
Adds a stuttering effect to your text, making it look like you're nervous or excited!

```python
from discordify import discordify

# Add stuttering effect
text = "Hello, how are you? I am fine, but tired."
stuttered = discordify.stutterify(text)
print(stuttered)
# Output: "H-Hello, how are y-you? I-I am fine, but... tired."
```

### 2. UwUify
Transforms your text into the cute "UwU" speak popular in some Discord communities.

```python
from discordify import discordify

# Make text cute and add sparkles
text = "Hello. How are you?"
uwu_text = discordify.uwuify(text)
print(uwu_text)
# Output: "✧˖°. hewwo˚｡⋆୨୧˚⋆˙⟡ how awe you? ₊˚⊹♡"
```

### 3. Leetify
Converts your text into "1337" (leet) speak by replacing letters with numbers.

```python
from discordify import discordify

# Convert to 1337 speak
text = "Hi, how are you?"
leet_text = discordify.leetify(text)
print(leet_text)
# Output: "H1, H0W 4R3 Y0U?"
```

### 4. Dummify
Reverses all vowels in your text for a silly transformation.

```python
from discordify import discordify

# Reverse vowels
text = "Hi, how are you?"
dummy_text = discordify.dummify(text)
print(dummy_text)
# Output: "Hu, how era yoi?"
```

### 5. Sarcasmify
Transforms text with alternating uppercase and lowercase letters to express sarcasm.

```python
from discordify import discordify

# Add sarcasm style
text = "Yeah, sure, whatever you say"
sarcasm_text = discordify.sarcasmify(text)
print(sarcasm_text)
# Output might be: "YeAh, SuRe, WhAtEvEr YoU sAy 🙄"
```
### 5. Piratify
Transforms text into a pirate speak.
```python
from discordify import discordify

# Add pirate speak
text = "Hello how are you"
pirate_text = discordify.piratify(text)
print(pirate_text)
# Output might be: "ahoy how be ye yarr harr! 🏴‍☠️"
```
## Command Line Usage

Discordify can also be used directly from the command line:

```bash
# Install the package
pip install discordify

# Run the CLI
discordify
```

Then follow the prompts to select a function and enter your text.

## Example Program

Here's a complete example program that demonstrates all functions:

```python
# example.py
from discordify import discordify

def demonstrate_discordify():
    sample_text = "Hello, world! Let's try all these transformations."
    
    print("Original text:")
    print(sample_text)
    print("\n1. Stutterify:")
    print(discordify.stutterify(sample_text))
    print("\n2. UwUify:")
    print(discordify.uwuify(sample_text))
    print("\n3. Leetify:")
    print(discordify.leetify(sample_text))
    print("\n4. Dummify:")
    print(discordify.dummify(sample_text))
    print("\n5. Sarcasmify:")
    print(discordify.sarcasmify(sample_text))

if __name__ == "__main__":
    demonstrate_discordify()
```

Save this as `example.py` and run it with `python example.py`.

## Development Setup

If you want to contribute to Discordify, follow these steps:

### Prerequisites

- Python 3.7 or higher
- pipenv

### Setup steps

1. Clone the repository:
   ```bash
   git clone https://github.com/software-students-spring2025/3-python-package-minesweepers.git
   cd 3-python-package-minesweepers
   ```

2. Set up the virtual environment and install dependencies:
   ```bash
   pipenv install --dev
   pipenv shell
   ```

3. Install the package in development mode:
   ```bash
   pipenv install -e .
   ```

### Running tests

We use pytest for testing. To run the tests:

```bash
pytest
```

### Building the package

To build the package:

```bash
python -m build
```

This will generate distribution files in the `dist/` directory.

### Workflow for contributions

1. Create a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and write tests if necessary

3. Run tests to ensure everything works:
   ```bash
   pytest
   ```

4. Commit your changes and push to your branch:
   ```bash
   git add .
   git commit -m "Add your meaningful commit message"
   git push origin feature/your-feature-name
   ```

5. Create a Pull Request to the `main` branch



