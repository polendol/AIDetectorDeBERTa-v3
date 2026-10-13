import os
import tempfile

import gradio as gr
from transformers import pipeline

os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

MODEL_ID = "vraj33/ai-text-detector-deberta"
CHUNK_SIZE = 2000  # characters (about 300-400 words)

# Loaded once when the app starts, not on every click.
pipe = pipeline("text-classification", model=MODEL_ID)

LABELS = {"LABEL_0": "AI", "LABEL_1": "Human"}


def analyse(file_path, progress=gr.Progress()):
    if file_path is None:
        raise gr.Error("Please upload a .txt file first.")

    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    if not content.strip():
        raise gr.Error("The uploaded file is empty.")

    chunks = [content[i:i + CHUNK_SIZE] for i in range(0, len(content), CHUNK_SIZE)]

    lines = [
        "AI DETECTION REPORT",
        f"Model used: {MODEL_ID}",
        f"Total Chunks: {len(chunks)}",
        "",
    ]

    for i, chunk in enumerate(progress.tqdm(chunks, desc="Analysing chunks")):
        # truncation=True stops the model from crashing on chunks longer than its token limit
        result = pipe(chunk, truncation=True)[0]
        label = LABELS.get(result["label"], "Unrecognised")
        preview = chunk[:100].replace("\n", " ")  # done outside the f-string (older Python can't put \n inside one)

        lines += [
            f"--- CHUNK {i + 1} ---",
            f"TEXT: {preview}...",
            f"LABEL:\n{label}\n",
            f"SCORE:\n{result['score']}\n",
            "*" * 50,
            "",
        ]

    report = "\n".join(lines)

    # Name the download after the uploaded file, e.g. essay.txt -> essay_report.txt
    base = os.path.splitext(os.path.basename(file_path))[0]
    out_path = os.path.join(tempfile.mkdtemp(), f"{base}_report.txt")
    with open(out_path, "w", encoding="utf-8") as out:
        out.write(report)

    return report, out_path


demo = gr.Interface(
    fn=analyse,
    inputs=gr.File(label="Upload a .txt file", file_types=[".txt"], type="filepath"),
    outputs=[
        gr.Textbox(label="Report preview", lines=20),
        gr.File(label="Download report (.txt)"),
    ],
    title="AI Text Detector",
    description="Upload a .txt file. The text is split into chunks and each chunk is labelled AI or Human.",
    flagging_mode="never",
)

if __name__ == "__main__":
    demo.launch()
