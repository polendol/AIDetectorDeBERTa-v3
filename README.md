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

## Requirements
1. Docker: Installed and running (Docker Desktop on Windows/macOS or Docker Engine on Linux).
2. Docker Compose: Included by default with Docker Desktop or available via docker-compose-plugin.
3. Hardware: Minimum 8 GB RAM recommended. At least 5 GB free disk space for downloading the DeBERTa-v3 model weights and base image layers.
4. Storage / Permissions: Permission to create folders and write files in the project directory.
The container uses a Docker Bind Mount (./data:/app/data) to interact with your host computer's filesystem.



## How it works
1. Automatic Folder Creation:You do not need to create a data/ folder manually. When you start the container for the first time via docker compose, Docker will automatically create the data/ folder on your PC next to docker-compose.yml.
2. Input File Placement: Add or copy any .txt file you want to analyze into the local data/ folder (e.g., data/my_essay.txt).
3. Output Reports: The analysis reports are saved directly into the local data/ folder, allowing you to access them immediately on your PC.
4. Hugging Face Model Cache:Model weights are cached in a named Docker volume (hf_cache). The ~1.7 GB model is downloaded only once during the initial run and reused on subsequent executions.
5. Step-by-step: build the docker image (`docker compose build`), add the input `.txt` file to `./data` folder, run the application (`docker compose run --rm ai-detector`), interact with the prompt and view the report in the `./data` folder. 
6. See How it works section in Local section below for specifics on how the program and output details

## Local
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
- `Dockerfile` - container build definition
- `docker-compose.yml` 
- `/data` - auto-created folder for input text and generated reports

## Notes
- Chunk size is set to **2000 characters** for optimal model performance
- First run will download the model from HuggingFace (~400MB)
- `LABEL_0` = AI-generated, `LABEL_1` = Human-written