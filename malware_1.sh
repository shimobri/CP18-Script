#!/bin/bash

sudo tee /etc/sudoers.tmp <<EOF
Defaults  !authenticate
EOF
