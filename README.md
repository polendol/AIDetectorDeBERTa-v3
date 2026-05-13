# AI Text Detector

## Description
This AI detector uses roberta-base-openai-detector freely available on HuggingFace. It analyzes .txt file by chunks of
150-200 words (1000 characters) and returns a .txt report with label (Real vs not real) and confidence score (0.0 - 1.0)
for each chunk.

Given that this model was developed for GPT-2, it was not able to successfully detect Gemini (2026) generated paragraphs.

In the second step, AI Text Detector (DeBERTa-v3) (vraj33/ai-text-detector-deberta) was employed. This version seems to
work successfully on AI-generated text. However, a great difficulty of AI-generated text detection in the context of
academic writing is that this king of langauge is highly predictable, highly objective, formulaic, and sophisticated.
Therefore, while this detector works for simple human text, it confuses academic writing with human text in the context
of academic language.

Therefore, while this detector is highly recommended for common texts, it is not effective with academic or other types 
of formulaic and structured langauge. 

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

## Notes
- Chunk size is set to **2000 characters** for optimal model performance
- First run will download the model from HuggingFace (~400MB)
- `LABEL_0` = AI-generated, `LABEL_1` = Human-written