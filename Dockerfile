# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run streamlit
CMD ["sh", "-c", "streamlit run app/streamlit_app.py --server.port=$PORT --server.address=0.0.0.0"]
