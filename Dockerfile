# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image

FROM pytorch/pytorch:latest

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# Get the Real World example app
RUN ls && echo sdfjskdflsjdf

# Set the working directory to /drf
# NOTE: all the directives that follow in the Dockerfile will be executed in
# that directory.
WORKDIR /app

COPY requirements.txt .


# RUN pip install torch==2.2.0+cpu  torchvision==0.17.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install -r requirements.txt


COPY . .

EXPOSE 80
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:80

