# MTAG container project

This repository is for containerization and distribution of `mtag` (Multi-Trait Analysis of GWAS) from [https://github.com/JonJala/mtag].

`mtag` is a Python-based command line tool for jointly analyzing multiple sets of GWAS summary statistics as described by [Turley et. al. (2018)](https://www.nature.com/articles/s41588-017-0009-4). 
It can also be used as a tool to meta-analyze GWAS results.

## Build status

[![License](http://img.shields.io/:license-GPLv3+-green.svg)](http://www.gnu.org/licenses/gpl-3.0.html)
[![Documentation Status](https://readthedocs.org/projects/mtag_container/badge/?version=latest)](https://mtag_container.readthedocs.io/en/latest/?badge=latest)
[![Flake8 lint](https://github.com/comorment/mtag_container/actions/workflows/python.yml/badge.svg)](https://github.com/comorment/mtag_container/actions/workflows/python.yml)
[![Dockerfile lint](https://github.com/comorment/mtag_container/actions/workflows/docker.yml/badge.svg)](https://github.com/comorment/mtag_container/actions/workflows/docker.yml)
[![Container build](https://github.com/comorment/mtag_container/actions/workflows/container_build.yml/badge.svg)](https://github.com/comorment/mtag_container/actions/workflows/container_build.yml)
[![Container build push](https://github.com/comorment/mtag_container/actions/workflows/container_build_push.yml/badge.svg)](https://github.com/comorment/mtag_container/actions/workflows/container_build_push.yml)

## Description of available packages

This repository provides the following [packages](https://github.com/orgs/comorment/packages?repo_name=mtag_container):

* ``mtag`` - a Docker container image with the `mtag` software set as entrypoint
* ``mtag_sif`` - A container on the Singularity Image Format (`.sif`) container file, suitable for use with Apptainer or Singularity/SingularityCE

## Software versions

Below is the list of tools included in the different Dockerfile(s) and installer bash scripts for each container.
Please keep up to date (and update the main `<mtag_container>/README.md` when pushing new container builds):

### Installation and set up

#### Dependencies on host system

In order to set up these resource, some software may be required

- [Singularity/SingularityCE](https://sylabs.io/singularity/) or [Apptainer](https://apptainer.org)
- [Git](https://git-scm.com/)
- [ORAS CLI](https://oras.land)

#### Clone the repository

To download the last revision of this project, issue:

```bash
cd path/to/repositories
git clone --depth 1 https://github.com/comorment/mtag_container.git
cd mtag_container
git pull  # optional, update to the latest version
```

#### Update the `mtag.sif` container

To obtain updated versions of the Singularity Image Format (.sif) container file for use with Apptainer or Singularity/SingularityCE, issue

```bash
cd path/to/repositories/mtag_container/apptainer
mv mtag.sif mtag.sif.old  # optional, just rename the old(er) file without overwriting
apptainer pull docker://ghcr.io/comorment/mtag:<tag>  # or
singularity pull docker://ghcr.io/comorment/mtag:<tag> # or 
oras pull ghcr.io/comorment/mtag_sif:<tag>
```

where `<tag>` corresponds to a tag listed under [packages](https://github.com/comorment/mtag_container/pkgs/container/mtag),
such as `latest`, `main`, or `sha_<GIT SHA>`. 
The `oras pull` statement pulls the `mtag_container.sif` file from [ghcr.io](https://github.com/comorment/mtag_container/pkgs/container/mtag_sif) using the [ORAS](https://oras.land) registry, without the need to build the container locally.

#### Using the `mtag.sif` container

To use the `mtag.sif` container with Apptainer, issue:

```bash
cd path/to/repositories/mtag_container/apptainer
export APPTAINER_BIND="<path/to/data>:/data"  # adapt as necessary to mount directories
apptainer exec mtag.sif mtag --help
```

See the Apptainer [documentation](https://apptainer.org/docs/user/main/bind_paths_and_mounts.html) for more information on mounting directories.
If using Singularity/SingularityCE, replace `apptainer` with `singularity` and `APPTAINER_BIND` with `SINGULARITY_BIND` in the above statement.

#### Pulling and using Docker image

To pull the corresponding Docker image, issue:

```bash
docker pull ghcr.io/comorment/mtag_container:<tag>
```

If working on recent Macs, add the `--platform=linux/amd64` after `docker pull`.
Using Docker may allow replacing `singularity exec ...` or `apptainer exec ...` statements with appropriate `docker run ...` statements,
on systems where Singularity or Apptainer is unavailable.
Functionally, the Docker image is equivalent to the Singularity container, but note that syntax for mounting volumes and invoking commands may differ.
Please refer to [docs.docker.com](https://docs.docker.com) for more information.

> [!NOTE] Note that the provided Docker image may not support all CPUs, and may not be able to run on all systems via CPU virtualization.
> An option may be to build the Docker image on the host machine (e.g., M1/M2 Macs, older Intel CPUs), as:
>
>```bash
>docker build --platform=linux/amd64 -t ghcr.io/comorment/mtag -f dockerfiles/mtag_container/Dockerfile .
>```

Example of using the Docker image:

```bash
#!/bin/bash
# define environment variables:
export IMAGE="ghcr.io/comorment/mtag:latest"  # adapt as necessary
# shortcut for mtag:
export MTAG="docker run --platform=linux/amd64 --rm -v ${PWD}:/home ${IMAGE}"
# invoke mtag's help function
$MTAG --help
```

For more information about mounting volumes/directories, see the Docker [documentation](https://docs.docker.com/engine/storage/volumes/).

### Systems without internet access

Some secure platforms do not have direct internet access, hence we recommend cloning/pulling all required files on a machine with internet access as explained above, and archive the `mtag_container` directory with all files and moving it using whatever file uploader is available for the platform.

```bash
cd /path/to/mtag_container
SHA=$(git rev-parse --short HEAD)
cd ..
tar --exclude=".git/*" -cvf mtag_container_$SHA.tar mtag_container
```

### mtag.sif
  
| OS/tool             | Version               | License           | Source
| ------------------- | --------------------- | ----------------- | -------------
| ubuntu              | 24.04                 | [Creative Commons CC-BY-SA version 3.0 UK licence](https://ubuntu.com/legal/intellectual-property-policy) | [Ubuntu.com](https://ubuntu.com)
| miniconda           | 4.7.12                | [BSD-3-Clause](https://docs.conda.io/en/latest/license.html) | [Miniconda](https://docs.anaconda.com/miniconda/)
| python              | 2.7.16                | [PSF](https://docs.python.org/2.7/license.html) | [Python.org](https://www.python.org)

## Building/rebuilding containers

While we don't recommend building containers locally, it is possible.
For instructions on how to build or rebuild containers manually using [Docker](https://www.docker.com) and [Singularity](https://docs.sylabs.io) refer to [`<mtag_container>/docker/README.md`](https://github.com/comorment/mtag_container/blob/main/docker/README.md).

## Unit tests

Unit tests are available in the `<mtag_container>/tests` directory. 
These are run using the [pytest](https://docs.pytest.org/en/stable/) framework, and part of the GitHub Actions workflow.
To run the tests locally, issue:

```bash
cd <mtag_container>
(pip install pytest)  # if not already installed
py.test -v tests
```

## Build the documentation

Within this repository, the html-documentation can be built from source files put here using [Sphinx](https://www.sphinx-doc.org/en/master/index.html). 
To do so, install Sphinx and some additional packages in Python using [Conda](https://docs.conda.io/en/latest/) by issuing:

```
cd <mtag_container>/docs/source
conda env create -f environment.yml  # creates environment "sphinx"
conda activate sphinx  # activates environment "sphinx
make html  # builds html documentation into _build/html/ subdirectory
```

The built documentation can be viewed locally in a web browser by opening the file 
`<mtag_container>/docs/source/_build/html/index.html`

The documentation may also be hosted online on [readthedocs.org](https://readthedocs.org).

## SLURM jobscript example

A basic job script example for running a Singularity container in an HPC setting with the [SLURM](https://slurm.schedmd.com) job scheduler is provided in the file [singularity_slurm_job.sh](https://github.com/comorment/mtag_container/blob/main/scripts/singularity_slurm_job.sh), and should be modified as needed.
It expects a few environment variables, and can be submitted as

```
export JOBNAME=mtag
export ACCOUNT=<project allocation account name>
export WALLTIME="01:00:00"  # expected run time HH:MM:SS format
export CPUS_PER_TASK=1  # number of CPU cores
export MEM_PER_CPU=2000MB  # RAM per CPU
export SINGULARITY_MODULE=singularity/3.7.1  # name of Singularity module and version

sbatch singularity_slurm_job.sh  # submit job
```
The output of the job will be written to the text files `mtag_container.out` (output) and `mtag_container.err` (errors).

## Feedback

If you face any issues, or if you need additional software, please let us know by creating a new [issue](https://github.com/comorment/mtag_container/issues/new).
