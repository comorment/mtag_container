all: mtag_container.sif  # additional .sif files may be listed here for corresponding dockerfiles

%.sif: dockerfiles/%/Dockerfile
	docker build -t $* -f dockerfiles/$*/Dockerfile . && \
	scripts/convert_docker_image_to_singularity.sh $* && \
	scripts/move_singularity_file.sh $*

# Example commands executed by this make file
# 
# Running "make mtag_container.sif" will issue the following commands:
# docker build -t mtag_container -f dockerfiles/mtag_container/Dockerfile . && \  # build docker container
#     scripts/convert_docker_image_to_singularity.sh mtag_container && \         # produces mtag_container.sif
#     scripts/move_singularity_file.sh.sh mtag_container        # moves mtag_container.sif to ../singularity/.
#  
# Running "make all" will build all singularity containers in this project
