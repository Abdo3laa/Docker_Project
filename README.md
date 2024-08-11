# Stop Words Remover

This project provides a Python script to process text files by removing stop words and counting the frequency of remaining words. It includes a Dockerfile to containerize the application.

## Project Overview

The `stopWordsRemover.py` script performs the following tasks:
- **Reads** a text file named `random_paragraphs.txt`.
- **Removes** predefined stop words from the text.
- **Counts** the frequency of the remaining words.
- **Displays** the word frequencies in the console.

## Python Script

### Overview
The core functionality is implemented in `stopWordsRemover.py`. Here's a summary of what the script does:

1. **Read the File**: Reads the content of `random_paragraphs.txt`.
2. **Remove Stop Words**: Filters out common stop words.
3. **Count Word Frequency**: Counts each remaining word's frequency.
4. **Display Results**: Outputs word frequencies to the console.

## Dockerfile

A Dockerfile is provided to containerize the application. It sets up a Python environment and executes the script within a Docker container.

### Dockerfile Description
- **Base Image**: Uses the official Python 3.9 slim image.
- **Working Directory**: Sets `/app` as the working directory.
- **File Copy**: Copies `stopWordsRemover.py` and `random_paragraphs.txt` into the container.
- **Port Exposure**: Exposes port 80.
- **Run Command**: Executes `stopWordsRemover.py` when the container starts.

## Instructions

### Prerequisites
- Docker installed on your machine.
- Python 3.9 or higher (if running the script outside Docker).

### Running the Script

**Locally:**
```bash
python stopWordsRemover.py
```
### Using Docker:
1. Build the Docker image:

```bash
docker build -t stop-words-remover .
```
2. Run the Docker container:

```bash
docker run -p 4000:80 stop-words-remover
```
3. Access the script’s output through the Docker container.

## Files Included
- **`stopWordsRemover.py`**: Python script for removing stop words and counting word frequencies.
- **`random_paragraphs.txt`**: Sample text file for processing.
- **`Dockerfile`**: Docker configuration file.
