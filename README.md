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

## Docker

### Requirements
1. **Docker:** Installed and running (Docker Desktop on Windows/macOS or Docker Engine on Linux).
2. **Docker Compose:** Included by default with Docker Desktop, or available via `docker-compose-plugin`.
3. **Hardware:** Minimum 8 GB RAM recommended. At least 5 GB of free disk space for the DeBERTa-v3 model weights and base image layers.
4. **Network:** Internet access on the first run, to download the model from Hugging Face.

### How it works
1. **Web interface:** The container runs a Gradio web app on port 7860. You upload a `.txt` file in your browser and download the report from the same page. No folders need to be created or mounted.
2. **Hugging Face model cache:** Model weights are cached in a named Docker volume (`hf_cache`). The ~1.7 GB model is downloaded only once, on the first run, and reused afterwards.
3. **Reports:** Each report is shown on the page and offered as a `.txt` download named after your file (e.g. `my_essay.txt` becomes `my_essay_report.txt`). Reports are not stored on your computer unless you download them.

### Step by step
1. Build and start the application:`docker compose up --build` 
2. Wait until the logs show that Gradio is running. The first start is slow because the model is downloading.
3. Open http://localhost:7860 in your browser.
4. Upload a `.txt` file, wait for the analysis to finish, and click the download link to save the report.


## Local
## Requirements
- Python 3.8+
- Internet connection to download the model

## Installation
pip install -r requirements.txt


## Usage
AI_detector_DeBERTa-v3


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
- `AI_detector_DeBERTa-v3.py` - main program, run this to launch the app (Gemma3:4b)
- `Human.txt` - file with an example of a text written by human (for testing)
- `reportXX.txt` - detection reports generated for each XX file
- `requirements.txt` — Python dependencies
- `README.md` — this file
- `Dockerfile` - container build definition
- `docker-compose.yml` 
- `/data` - auto-created folder for input text and generated reports
- `app.py` - gradio interface



 ## License & Attributions

### Model & Third-Party Attributions
* **Model Weights:** Uses [`vraj33/ai-text-detector-deberta`](https://huggingface.co/vraj33/ai-text-detector-deberta) hosted on Hugging Face. The underlying architecture is based on [Microsoft DeBERTa-v3](https://huggingface.co/microsoft/deberta-v3-base) (licensed under MIT).
* **Interface & Frameworks:** Built using [Gradio](https://github.com/gradio-app/gradio) (Apache 2.0 License).


## Notes
- Chunk size is set to **2000 characters** for optimal model performance
- First run will download the model from HuggingFace (~400MB)
- `LABEL_0` = AI-generated, `LABEL_1` = Human-written
