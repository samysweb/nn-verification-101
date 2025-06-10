FROM jupyter/base-notebook:python-3.9

# Upgrade pip to the latest version
RUN pip install --upgrade pip
# Install DNNV
RUN pip install dnnv

USER root

RUN apt update && apt install -y build-essential software-properties-common cmake git curl
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

USER jovyan

# Install ERAN and MIPVerify
RUN dnnv_manage install mipverify eran
