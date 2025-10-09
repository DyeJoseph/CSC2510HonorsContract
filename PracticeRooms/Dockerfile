#start pulling the pythin image
FROM python:3.13.7-alpine

#switch working directories
WORKDIR /app

#install system dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev

#copy the requirements file into the image
COPY requirements.txt .

#install the dependencies and packages in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

#copy every content from the local file to the image
COPY . .

#configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["practiceRooms.py"]