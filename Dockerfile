# Use an official Python 3.11 runtime as a parent image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install virtualenv
RUN python -m venv /env

# Activate the virtual environment and install dependencies
ENV VIRTUAL_ENV=/env
ENV PATH="/env/bin:$PATH"

# Copy the application's requirements.txt and run pip to install all dependencies into the virtualenv
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code
COPY . ./

# Expose the port the app runs on
EXPOSE 8080

# Run a WSGI server to serve the application. Ensure gunicorn is declared as a dependency in requirements.txt
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:server"]

