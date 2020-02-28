FROM python:3

LABEL maintainer="Benjamin Wallace <me@bcwallace.com>"

WORKDIR /

COPY . ./
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]