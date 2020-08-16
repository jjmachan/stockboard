# set base image (host OS)
FROM python:3.7

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY api/ .

# command to run on container start
CMD ["uvicorn", "main:stockboard", "--host", "0.0.0.0", "--port", "8000"]
