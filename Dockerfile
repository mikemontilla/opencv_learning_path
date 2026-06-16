FROM python:3.11-slim

WORKDIR /workspace

COPY requirements.txt .
RUN pip install --default-timeout=120 --retries=10 -r requirements.txt

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.disable_check_xsrf=True"]
