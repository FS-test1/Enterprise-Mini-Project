FROM python:3.9.6-bullseye
WORKDIR /usr/src/main
COPY . .
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py", "-m", "flask", "run", "--host=0.0.0.0", "--port", "8000"]
#CMD ["main.py"]
#ENTRYPOINT ["PYTHON3"]