#
# Copyright (C) 2020 by ItzSjDude@Github, < https://github.com/ItzSjDude/PikachuUserbot >.
#
# This file is part of < https://github.com/ItzSjDude/PikachuUserbot > project,
# and is released under the "GNU v3.0 License Agreement".
# 
# Please see < https://github.com/ItzSjDude/PikachuUserbot/blob/master/LICENSE >
#
# All rights reserved 

FROM kalilinux/kali-rolling
ARG DEBIAN_FRONTEND=noninteractive
COPY script.sh /tmp/script.sh
WORKDIR root/ItzSjDude
RUN /tmp/script.sh && chmod +x /usr/local/bin/* 
