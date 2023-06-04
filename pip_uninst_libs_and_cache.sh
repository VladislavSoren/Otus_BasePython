#!/bin/bash

# graceful removal of libraries
pip freeze | xargs pip uninstall -y

# pip cache purge
pip cache purge
