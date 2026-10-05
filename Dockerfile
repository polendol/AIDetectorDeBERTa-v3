FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    HF_HOME=/home/appuser/.cache/huggingface \
    GRADIO_SERVER_NAME=0.0.0.0 \
    GRADIO_SERVER_PORT=7860

WORKDIR /app

COPY requirements.txt .
# CPU-only torch first (much smaller), then the rest
RUN pip install --index-url https://download.pytorch.org/whl/cpu torch \
 && pip install -r requirements.txt

RUN useradd --create-home --uid 1001 appuser \
 && mkdir -p /home/appuser/.cache/huggingface \
 && chown -R appuser:appuser /app /home/appuser/.cache
USER appuser

COPY --chown=appuser:appuser . .

EXPOSE 7860

CMD ["python", "app.py"]