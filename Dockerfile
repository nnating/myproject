FROM python:3.6
RUN mkdir /myproject
WORKDIR /myproject
COPY . .
RUN python -m pip install --upgrade pip \
  && pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]