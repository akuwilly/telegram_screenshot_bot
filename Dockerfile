FROM python:3.10-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    ca-certificates \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Set environment
ENV CHROME_BIN=/usr/bin/google-chrome
ENV PATH="$PATH:/usr/bin"

# Set working dir
WORKDIR /app

# Copy project files
COPY . .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Default command
CMD ["python", "bot_schedule.py"]
