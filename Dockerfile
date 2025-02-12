# Use the official Apache Airflow image as the base image
FROM apache/airflow:2.10.5

# Set the working directory to /opt/airflow
WORKDIR /opt/airflow

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
