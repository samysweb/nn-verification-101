FROM jupyter/base-notebook:python-3.9

# Upgrade pip to the latest version
RUN pip install --upgrade pip
# Install DNNV
RUN pip install dnnv
# Install ERAN and MIPVerify
RUN dnnv_manage install mipverify eran
