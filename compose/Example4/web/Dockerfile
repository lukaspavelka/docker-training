FROM python:3.9-slim

LABEL maintainer="Lukas Pavelka (updated by AI Assistant)"

WORKDIR /app

# Copy application code
# Using COPY instead of ADD as it's more explicit for simple file copies
COPY ./index.py /app/index.py
# If there were other files like templates or static assets, copy them too.
# e.g. COPY ./static /app/static

# No requirements.txt needed for this simple built-in server,
# but if it had dependencies:
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the application will run on (matches CMD and internal port in compose file)
EXPOSE 8000

# Command to run the application
# Ensure index.py is executable if it has a shebang and is run directly,
# or call python explicitly.
CMD ["python", "index.py"]
