# AI Text Detector

## Description
This AI detector stems from a need to ensure no traces of AI-generated text are found in academic texts. Given that 
papers in preparation are privacy-sensitive, this programs ensures that files can be evaluated for AI-generated text 
without submitting them to currently available online programs.

This AI detector uses DoBERTa-v3 (`vraj33/ai-text-detector-deberta`) model freely available on HuggingFace. It analyzes .txt file by chunks of
150-200 words (1000 characters) and returns a .txt report with label (Real vs not real) and confidence score (0.0 - 1.0)
for each chunk.

However, a great difficulty of AI-generated text detection in the context of academic writing is that this king of langauge is highly predictable, highly objective, formulaic, and sophisticated.
Therefore, while this detector works for simple human text, it confuses academic writing with human text in the context
of academic language.


## Requirements
- Python 3.8+
- Internet connection to download the model

## Installation
pip install -r requirements.txt


## Usage
AI_detector_DoBERTa-v3


Enter the input file name 
Enter the name of .txt report that will be generated


## Output
Generates a `.txt` report with per-chunk analysis:
- **LABEL**: `AI` or `Human`
- **SCORE**: Model confidence (0.0 – 1.0)
 
## How It Works
1. Reads the input `.txt` file
2. Splits the text into chunks of ~2000 characters (~300–400 words)
3. Runs each chunk through the DeBERTa classifier
4. Writes a full report to the output `.txt` file

## Files Structure
- `AI_detector_DoBERTa-v3.py` - main program, run this to launch the app (Gemma3:4b)
- `AI.txt` - file with an example short AI-generated text (for testing)
- `Human.txt` - file with an example of a text written by human (for testing)
- `CJAL.txt` - authentic paper where human and AI generated text is mixed (for testing)
- `reportXX.txt` - detection reports generated for each XX file
- `requirements.txt` — Python dependencies
- `README.md` — this file

## Notes
- Chunk size is set to **2000 characters** for optimal model performance
- First run will download the model from HuggingFace (~400MB)
- `LABEL_0` = AI-generated, `LABEL_1` = Human-written