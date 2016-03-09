@echo off

set KEY_FILE=~/.ssh/id_rsa
bash -c "eval `ssh-agent`; ssh-add; vagrant ssh airflow-local -- -t '. /etc/profile; bash -l'"
