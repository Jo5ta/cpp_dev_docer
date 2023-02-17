FROM bitnami/minideb:latest

USER root
RUN apt update && apt install -y \
    gcc-10\
    gcc-10-multilib\
    gcc-10-plugin-dev\
    g++-10\
    clang\
    clang-format\
    lldb\
    python3\
    python3-pip\
    git\
    git-lfs\
    gdb\
    curl\
    cmake\
    ninja-build\
    make\
    ;

RUN useradd -m cpp_dev_docker
USER cpp_dev_docker