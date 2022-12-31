FROM python:3.9-slim

# switch working directory


WORKDIR /app

# install the dependencies and packages in the requirements file
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# copy every content from the local file to the image
COPY . .

CMD [ "python3", "main.py"]
