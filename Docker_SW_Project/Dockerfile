# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY stopWordsRemover.py /app/
COPY random_paragraphs.txt /app/


# Make port 80 available to the world outside this container
EXPOSE 80

# Run the Python script when the container launches
CMD ["python", "stopWordsRemover.py"]

