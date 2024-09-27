# container_template project

README info goes here. Modify for your own project's needs.

# Important! - post initial setup steps

After setting up your project from the template, add files, commit and push the changes after running the setup script (`scripts/init.py`):

```
git add <file1> <file2> ...
git commit -a -m "initial setup"
git push
```

The remaining codes may then be added to and be modified further to suit the requirements of the `<container_template>` project. 

# Important! - Set up Git LFS

Container files may get large and one should never add large binary files (.sif, .zip, .tar.gz, .mat, .dat, etc.) in [git](https://git-scm.com) repositories directly, mainly files that can be parsed as raw text files (code files, etc.).
[**Git Large File Storage** (LFS)](https://git-lfs.github.com) should be used instead.
Before adding new files to this project after initialization (running `python scripts/init.py`), go through step 1-3 on the Git LFS [homepage](https://git-lfs.github.com).
Revise the `<container_template>/.gitattributes` file as necessary. Some common file formats has been added already.

## Build status

[![License](http://img.shields.io/:license-GPLv3+-green.svg)](http://www.gnu.org/licenses/gpl-3.0.html)
[![Documentation Status](https://readthedocs.org/projects/container-template/badge/?version=latest)](https://container-template.readthedocs.io/en/latest/?badge=latest)
[![Flake8 lint](https://github.com/precimed/container_template/actions/workflows/python.yml/badge.svg)](https://github.com/precimed/container_template/actions/workflows/python.yml)
[![Dockerfile lint](https://github.com/precimed/container_template/actions/workflows/docker.yml/badge.svg)](https://github.com/precimed/container_template/actions/workflows/docker.yml)
[![Container build](https://github.com/precimed/container_template/actions/workflows/container_build.yml/badge.svg)](https://github.com/precimed/container_template/actions/workflows/container_build.yml)
[![Container build push](https://github.com/precimed/container_template/actions/workflows/container_build_push.yml/badge.svg)](https://github.com/precimed/container_template/actions/workflows/container_build_push.yml)

## Description of available containers

* ``container_template`` - a hello-world introductory container setup

## Software versions

Below is the list of tools included in the different Dockerfile(s) and installer bash scripts for each container.
Please keep up to date (and update the main `<container_template>/README.md` when pushing new container builds):

### Installation and set up

#### Dependencies on host system

In order to set up these resource, some software may be required

- [Singularity/SingularityCE](https://sylabs.io/singularity/) or [Apptainer](https://apptainer.org)
- [Git](https://git-scm.com/)
- [Git LFS](https://git-lfs.com)
- [ORAS CLI](https://oras.land)

#### Clone the repository

To download the last revision of this project, issue:

```bash
cd path/to/repositories
git clone --depth 1 https://github.com/precimed/container_template.git
cd container_template
git lfs pull  # pull "large" files
```

#### Update the `container_template.sif` container

To obtain updated versions of the Singularity Image Format (.sif) container file `, issue

```bash
cd path/to/repositories/container_template/singularity
mv container_template.sif container_template.sif.old  # optional, just rename the old(er) file
apptainer pull docker://ghcr.io/precimed/container_template:<tag>  # or
singularity pull docker://ghcr.io/precimed/container_template:<tag> # or 
oras pull ghcr.io/precimed/container_template_sif:<tag>
```

where `<tag>` corresponds to a tag listed under [packages](https://github.com/precimed/container_template/pkgs/container/container_template),
such as `latest`, `main`, or `sha_<GIT SHA>`. 
The `oras pull` statement pulls the `container_template.sif` file from [ghcr.io](https://github.com/precimed/container_template/pkgs/container/container_template_sif) using the [ORAS](https://oras.land) registry, without the need to build the container locally.

#### Pulling and using Docker image

To pull the corresponding Docker image, issue:

```bash
docker pull ghcr.io/precimed/container_template:<tag>
```

If working on recent Macs, add the `--platform=linux/amd64` after `docker pull`. 
This may allow replacing `singularity exec ...` or `apptainer exec ...` statements with appropriate `docker run ...` statements, 
on systems where Singularity or Apptainer is unavailable.
Functionally, the Docker image is equivalent to the Singularity container, but note that syntax for mounting volumes and invoking commands may differ.
Please refer to [docs.docker.com](https://docs.docker.com) for more information.

> [!NOTE] Note that the provided Docker image may not support all CPUs, and may not be able to run on all systems via CPU virtualization.
> An option may be to build the Docker image on the host machine (e.g., M1/M2 Macs, older Intel CPUs), as:
>
>```bash
>docker build --platform=linux/amd64 -t ghcr.io/precimed/container_template -f dockerfiles/container_template/Dockerfile .
>```

Example of using the Docker image:

```bash
#!/bin/bash
# define environment variables:
export IMAGE="ghcr.io/precimed/container_template:latest"  # adapt as necessary
# shortcuts for Python and interactive shell:
export PYTHON="docker run --platform=linux/amd64 --rm -v ${PWD}:/home -w/home --entrypoint=python ${IMAGE}"
export ISHELL="docker run --platform=linux/amd64 --rm -it -v ${PWD}:/home -w/home --entrypoint=bash ${IMAGE}"

# invoke Python help/list local directory
$PYTHON --help
$PYTHON -c "import os; print(os.listdir())"
```

### Systems without internet access

Some secure platforms do not have direct internet access, hence we recommend cloning/pulling all required files on a machine with internet access as explained above, and archive the `container_template` directory with all files and moving it using whatever file uploader is available for the platform.

```bash
cd /path/to/container_template
SHA=$(git rev-parse --short HEAD)
cd ..
tar --exclude=".git/*" -cvf container_template_$SHA.tar container_template
```

### container_template.sif
  
| OS/tool             | Version               | License           | Source
| ------------------- | --------------------- | ----------------- | -------------
| ubuntu              | 24.04                 | [Creative Commons CC-BY-SA version 3.0 UK licence](https://ubuntu.com/legal/intellectual-property-policy) | [Ubuntu.com](https://ubuntu.com)
| mambaforge          | 24.7.1-0              | [BSD-3-Clause](https://github.com/conda-forge/miniforge/blob/main/LICENSE) | [MiniForge](https://github.com/conda-forge/miniforge)
| python              | 3.12.5                | [PSF](https://docs.python.org/3.10/license.html) | [Python.org](https://www.python.org)

## Building/rebuilding containers

While we don't recommend building containers locally, it is possible.
For instructions on how to build or rebuild containers manually using [Docker](https://www.docker.com) and [Singularity](https://docs.sylabs.io) refer to [`<container_template>/docker/README.md`](https://github.com/precimed/container_template/blob/main/docker/README.md).

## Unit tests

Unit tests are available in the `<container_template>/tests` directory. 
These are run using the [pytest](https://docs.pytest.org/en/stable/) framework, and part of the GitHub Actions workflow.
To run the tests locally, issue:

```bash
cd <container_template>
(pip install pytest)  # if not already installed
py.test -v tests
```

## Build the documentation

Within this repository, the html-documentation can be built from source files put here using [Sphinx](https://www.sphinx-doc.org/en/master/index.html). 
To do so, install Sphinx and some additional packages in Python using [Conda](https://docs.conda.io/en/latest/) by issuing:

```
cd <container_template>/docs/source
conda env create -f environment.yml  # creates environment "sphinx"
conda activate sphinx  # activates environment "sphinx
make html  # builds html documentation into _build/html/ subdirectory
```

The built documentation can be viewed locally in a web browser by opening the file 
`<container_template>/docs/source/_build/html/index.html`

The documentation may also be hosted online on [readthedocs.org](https://readthedocs.org).

## SLURM jobscript example

A basic job script example for running a Singularity container in an HPC setting with the [SLURM](https://slurm.schedmd.com) job scheduler is provided in the file [singularity_slurm_job.sh](https://github.com/precimed/container_template/blob/main/scripts/singularity_slurm_job.sh), and should be modified as needed.
It expects a few environment variables, and can be submitted as

```
export JOBNAME=container_template
export ACCOUNT=<project allocation account name>
export WALLTIME="00:05:00"  # expected run time HH:MM:SS format
export CPUS_PER_TASK=1  # number of CPU cores
export MEM_PER_CPU=2000MB  # RAM per CPU
export SINGULARITY_MODULE=singularity/3.7.1  # name of Singularity module and version

sbatch singularity_slurm_job.sh  # submit job
```
The output of the job will be written to the text files `container_template.out` (output) and `container_template.err` (errors).

## Feedback

If you face any issues, or if you need additional software, please let us know by creating a new [issue](https://github.com/precimed/container_template/issues/new).
