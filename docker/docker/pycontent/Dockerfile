FROM python:3.7

WORKDIR /app

ENV ANSIBLE_VAULT_PASSWORD_FILE=/.vault_pass

# Install runtime deps into pkg deployment dir
COPY docker/pycontent/requirements.txt /app/img-requirements.txt
RUN pip install --requirement /app/img-requirements.txt

COPY setup.py /app/setup.py
COPY src/* /app/src

RUN python setup.py bdist_wheel
RUN pip install \ 
  --no-index \
  --find-links dist \
  pycontent 
