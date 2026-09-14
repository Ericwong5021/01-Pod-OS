FROM ubuntu:18.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates curl git gnupg python python3 openjdk-8-jdk build-essential gcc-multilib g++-multilib flex bison gperf zip unzip rsync bc ccache libssl-dev libxml2-utils xsltproc libncurses5 libncurses5-dev lib32z1-dev lib32ncurses5-dev zlib1g-dev x11proto-core-dev libx11-dev libgl1-mesa-dev fontconfig
RUN git clone --depth 1 --branch v2.32 https://gerrit.googlesource.com/git-repo /opt/git-repo
ENV PATH=/opt/git-repo:$PATH
ENV LANG=C.UTF-8
