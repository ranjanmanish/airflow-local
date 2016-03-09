# airflow-local

* Source code - [Github][10]
* Author - Gavin Noronha - <gavinln@hotmail.com>

[1]: https://github.com/gavinln/airflow-local.git

## About

This project provides a [Ubuntu (14.04)][20] [Vagrant][30] Virtual Machine (VM) with [Airflow][40], a data workflow management system from [Airbnb][50].

[20]: http://releases.ubuntu.com/14.04/
[30]: http://www.vagrantup.com/
[40]: https://github.com/airbnb/airflow
[50]: http://nerds.airbnb.com/airflow/

There are [Puppet][60] scripts that automatically install the software when the VM is started.

[60]: http://puppetlabs.com/

## Running

1. To start the virtual machine(VM) type

    ```
    vagrant up airflow-local
    ```

2. Connect to the VM

    ```
    vagrant ssh airflow-local
    ```

4. Open the notebook in the browser at the URL.

    ```
    http://192.168.33.10:8080/
    ```

## Requirements

The following software is needed to get the software from github and run
Vagrant to set up the Python development environment. The Git environment
also provides an [SSH  client][200] for Windows.

* [Oracle VM VirtualBox][210]
* [Vagrant][220]
* [Git][230]

[200]: http://en.wikipedia.org/wiki/Secure_Shell
[210]: https://www.virtualbox.org/
[220]: http://vagrantup.com/
[230]: http://git-scm.com/
