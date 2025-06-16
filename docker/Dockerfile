FROM jupyter/base-notebook:python-3.9

USER root

RUN apt update && apt install -y build-essential software-properties-common cmake git curl
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

USER jovyan

# Upgrade pip to the latest version
RUN pip install --upgrade pip
# Install DNNV
RUN pip install dnnv

# dnnv_manage assumes this folder exists already
# (most likely because one usually installs a tool first which does not require Gurobi?)
RUN mkdir -p /home/jovyan/.local/share/dnnv/bin
# Need to add path manually to make sure dnnv correctly finds its tools
ENV PATH="$PATH:/home/jovyan/.local/share/dnnv/bin"
# Make Julia's precompilation Docker-friendly
# (possibly running on different "sub-architectures")
ENV JULIA_CPU_TARGET=generic

# Install ERAN and MIPVerify
RUN dnnv_manage install mipverify eran

COPY mipverify_init.py /opt/conda/lib/python3.9/site-packages/dnnv/verifiers/mipverify/__init__.py
COPY mipverify_utils.py /opt/conda/lib/python3.9/site-packages/dnnv/verifiers/mipverify/utils.py
