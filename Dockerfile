#
# Copyright (C) 2020 by ItzSjDude@Github, < https://github.com/ItzSjDude/PikachuUserbot >.
#
# This file is part of < https://github.com/ItzSjDude/PikachuUserbot > project,
# and is released under the "GNU v3.0 License Agreement".
# 
# Please see < https://github.com/ItzSjDude/PikachuUserbot/blob/master/LICENSE >
#
# All rights reserved 

FROM ubuntu:latest
RUN apt-get update && apt-get install wget -y && wget https://raw.githubusercontent.com/ItzSjDude/PikabotHelper/main/pika.sh
COPY pika.sh /pika.sh
WORKDIR root/ItzSjDude
RUN chmod -x /pika.sh && /pika.sh && chmod +x /usr/local/bin/* 
