# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies for Poetry
RUN apt-get update && apt-get install -y \
    curl \
    && apt-get clean

# Install Poetry
RUN pip install poetry

COPY pyproject.toml .
RUN poetry config virtualenvs.create false
RUN poetry install

# Copy the rest of the application code to the working directory
COPY . /app

# Expose the Streamlit default port
EXPOSE 8501

# Set the command to run the Streamlit app
CMD ["streamlit", "run", "main.py"]
