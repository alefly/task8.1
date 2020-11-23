FROM python:3
RUN pip install --upgrade pip && \
    pip install flask
COPY copy .
CMD ["python", "./server.py"]
VOLUME /var/log
EXPOSE 8080
