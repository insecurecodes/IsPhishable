FROM python:3.7-slim-buster

# Set the working directory
WORKDIR /app

# Copy the script and requirements file to the container
COPY IsPhishable.py .
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt


# Set the entrypoint command for the container
ENTRYPOINT ["python","IsPhishable.py"]