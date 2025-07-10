
FROM python:3.9-slim-buster


WORKDIR /app


COPY ./app/requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org


COPY ./app .


EXPOSE 8000


CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]