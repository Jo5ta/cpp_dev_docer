# C++ Development Docker Image

This Docker image provides a development environment for C++ applications, with the following tools and libraries pre-installed:

- `gcc-10`
- `g++-10`
- `clang`
- `clang-format`
- `lldb`
- `python3` and `python3-pip`
- `git` and `git-lfs`
- `gdb`
- `curl`
- `cmake`
- `ninja-build`
- `make`

## Usage

To use this Docker image, you can either download it from Docker Hub or build it yourself.

### Download from Docker Hub

You can download the latest version of this Docker image from Docker Hub by running the following command:

```
docker pull jo5ta/cpp_dev_docker
```

### Build the image

To build the Docker image yourself, you can use the following commands:

```
git clone https://github.com/your-github-username/your-repo-name.git
cd your-repo-name
docker build -t cpp_dev_docker .
```

This will clone your repository, navigate to its directory, and build the Docker image using the `Dockerfile` provided in the repository.

### Running the container

Once you have the Docker image, you can run it using the following command:

```
docker run -it --name cpp_dev_container jo5ta/cpp_dev_docker
```

This will start a new container using the Docker image, with an interactive shell (`-it`) and the name `cpp_dev_container`.

### Creating a user and home folder

The Docker image includes a `cpp_dev_docker` user, which you can use to run your applications. To create a new user and home folder, you can run the following command:

```
docker run -it --name cpp_dev_container --user root jo5ta/cpp_dev_docker /bin/bash -c "useradd -m myuser && su myuser"
```

This will create a new user named `myuser` and switch to that user's home directory.

