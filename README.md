# Chippy: A minimal prompting interface for Chip

Chippy provides a minimal prompting interface for chip_1.4B_instruct_alpha, a new experimental instruction tuned model based on pythia-1.4B-deduped. With Chippy, you can easily prompt user input via Streamlit and FastAPI.

## Installation

To install Chippy's dependencies, you can use `pip`. Simply run the following command in your terminal:

```bash
pip install -r requirements.txt
```

## Starting FastAPI

```bash
python api.py --host "127.0.0.1" --port 8000
```

## Launching Streamlit

```bash
python app.py
```

## Current limitations of this demo app:

- Only single turn, no conversations yet
- This also means that the model won't remember previous prompts
- GPU only, minimum 8GB (CPU would be possible, but I found it to be way too slow)
- Hardcoded (decent) generation settings
- No support for the bigger versions of chip since this repo is targeted towards consumer hardware

For more information, check out the model card on Huggingface: https://huggingface.co/Rallio67/chip_1.4B_instruct_alpha

Thanks to LAION contributors and Stability.ai for making this possible.