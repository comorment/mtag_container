all: container_template.sif  # additional .sif files may be listed here for corresponding dockerfiles

%.sif: dockerfiles/%/Dockerfile
	docker build -t $* -f dockerfiles/$*/Dockerfile . && \
	scripts/convert_docker_image_to_singularity.sh $* && \
	scripts/move_singularity_file.sh $*

# Example commands executed by this make file
# 
# Running "make container_template.sif" will issue the following commands:
# docker build -t container_template -f dockerfiles/container_template/Dockerfile . && \  # build docker container
#     scripts/convert_docker_image_to_singularity.sh container_template && \         # produces container_template.sif
#     scripts/move_singularity_file.sh.sh container_template        # moves container_template.sif to ../singularity/.
#  
# Running "make all" will build all singularity containers in this project
