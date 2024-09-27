# Source files

## Singularity containers

This repository is used to develop and document [Docker](https://www.docker.com) and [Singularity](https://docs.sylabs.io) containers with various software and analytical tools.

## Software versions

  Below is the list of tools included in the different Dockerfiles and installer bash scripts for each container.
  Please keep up to date (and update the main `<mtag_container>/README.md` when pushing new container builds):

### mtag_container.sif
  
| OS/tool             | Version               | License           | Source
| ------------------- | --------------------- | ----------------- | -------------
| ubuntu              | 20.04                 | [Creative Commons CC-BY-SA version 3.0 UK licence](https://ubuntu.com/legal/intellectual-property-policy) | [Ubuntu.com](https://ubuntu.com)
| Mambaforge          | Mambaforge-22.11.1-4  | [BSD-3-clause](https://github.com/conda-forge/miniforge/blob/main/LICENSE) | [github.com/conda-forge/miniforge](https://github.com/conda-forge/miniforge)
| python              | 3.10.6                | [PSF](https://docs.python.org/3.10/license.html) | [Python.org](https://www.python.org)

## Feedback

If you face any issues, or if you need additional software, please let us know by creating an [issue](https://github.com/espenhgn/mtag_container/issues/new).

## Build instructions – DEPRECATED

The build scripts described below are deprecated and will be removed in the future.
We rely on a GitHub Actions workflow to build the containers and push them to the GitHub Container Registry.
See the [GitHub Actions](../.github/workflows/container_build_push.yml) file for more information.

### The easy(er) way

For convenience, a `Makefile` is provided in this directory in order to build [Singularity](https://docs.sylabs.io) containers from Dockerfiles (as `<mtag_container/docker/dockerfiles/mtag_container/Dockerfile>`).
Using this files assumes that a working [Docker](https://www.docker.com) and [Singularity](https://docs.sylabs.io) installation, as well as the [`GNU make`](https://www.gnu.org/software/make/) utility is available on the host computer/build system.
On Debian-based Linux OS, this utility can usually be installed by issuing`apt-get install -y make`; on MacOS with [Homebrew](https://brew.sh) as`brew install make`. Prefix`sudo` if necessary.

Then, the container can be built by issuing:

```
make mtag_container.sif
```

If all went well, the built file should be located as `<mtag_container/containers/mtag_container.sif>`.
In case super-user (`sudo`) privileges are required, issue:

```
sudo make mtag_container.sif
```

### Manual builds

In order to build the container manually, this is possible via the following steps

```
docker build -t mtag_container -f dockerfiles/mtag_container/Dockerfile .  # build docker container
```

In case you do not want to use Singularity (e.g., for testing locally), the build can be used e.g., by issuing

```
docker run -it -p 5001:5001 mtag_container python --version
```

which should return the currently installed Python version incorporated into the container.
You may replace the port numbers (``5001``) by another (e.g., ``5000``).

To convert, and relocate the Singularity container file generated from the Docker image, issue

```
bash scripts/convert_docker_image_to_singularity.sh mtag_container  # produces mtag_container.sif
bash scripts/scripts/move_singularity_file.sh.sh mtag_container  # put mtag_container.sif file to <mtag_container>/containers/ directory
```

Again, super-user (`sudo`) privileges may be required on the host computer. In that case, prefix `sudo` on the line(s) that fail.
For further details on the commands within each bash file, open the ``.sh`` files in a code editor.

### Clean up

The above steps may leave a collection of images in the Docker registry, wasting drive space.
To list them, issue

```
docker images -a
```

Chosen images can be removed by issuing:

```
docker rmi <image-id-1> <image-id-2> ... 
```

For more info, see [`docker rm`](https://docs.docker.com/engine/reference/commandline/rm/)

## Testing container builds

Some basic checks for the functionality of the different container builds are provided in `<mtag_container>/tests/`, implemented in Python.
The tests can be executed using the [Pytest](https://docs.pytest.org) testing framework.

In case `singularity` is not found in `PATH`, tests will fall back to `docker`.
In case `docker` is not found, no tests will run.

To install Pytest in the current Python environment, issue:

```
pip install pytest  # --user optional
```

New virtual environment using [conda](https://docs.conda.io/en/latest/index.html):

```
conda create -n pytest python=3 pytest -y  # creates env "pytest"
conda activate pytest  # activates env "pytest"
```

Then, all checks can be executed by issuing:

```
cd <mtag_container>
py.test -v tests  # with verbose output
```

Checks for individual containers (e.g., `mtag_container.sif`) can be executed by issuing:

```
py.test -v tests/test_mtag_container.py
```

Note that the proper container files (*.sif files) corresponding to the different test scripts must exist in `<mtag_container>/containers/`,
not only git LFS pointer files.
