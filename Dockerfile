FROM nikolaik/python-nodejs:python3.10-nodejs19

# Install required system packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy codebase to container
COPY . /app/
WORKDIR /app/

# Install Python dependencies
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Expose port for webhook (Render uses PORT env variable)
ENV PORT 8080
EXPOSE 8080

# Launch app using Python
CMD ["python3", "-m", "TheRapNation"]
