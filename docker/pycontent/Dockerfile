FROM python:3.7

WORKDIR /app

ENV ANSIBLE_VAULT_PASSWORD_FILE=/.vault_pass

# Install runtime deps into pkg deployment dir
RUN pwd
COPY docker/pycontent/requirements.txt /app/img-requirements.txt
RUN pip install --requirement /app/img-requirements.txt
