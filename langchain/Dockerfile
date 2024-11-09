#Deriving the latest base image
FROM python:3.12-slim


#Labels as key value pair
LABEL Maintainer="learning-bos"


# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /app

#to COPY the remote file at working directory in container
COPY . .
# Now the structure looks like this '/usr/app/src/test.py'

RUN pip3 install --no-cache-dir -r requirements.txt --user
#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python", "langchain.py"]