#!/bin/bash

exec_as_user() {
  # define inside function so that we won't get Permission error with
  # /root/bash_profile
  local USERNAME='myuser'

  # create a user and allow sudo without password,
  # also supress this block's ouput
  {
    adduser --disabled-password --gecos '' $USERNAME &&
    adduser $USERNAME sudo &&
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
  } &> /dev/null

  # this user needs PATH env of root user, it is the reason behind
  # 'DJANGO_SETTINGS_MODULE variable not defined' errors on normal users
  # without proper PATH varibles
  echo export PATH=$PATH >> /etc/environment
  # switch to created user, source the PATH variable
  # and execute the command passed in ('$@' won't work with below command)
  su -m $USERNAME -c "source /etc/environment && $*"
}

exec_as_user "$@"
