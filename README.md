# airflow-local

* Source code - [Github][10]
* Author - Gavin Noronha - <gavinln@hotmail.com>

[10]: https://github.com/gavinln/airflow-local.git

## About

This project provides a [Ubuntu (14.04)][20] [Vagrant][30] Virtual Machine (VM) with [Airflow][40], a data workflow management system from [Airbnb][50].

[20]: http://releases.ubuntu.com/14.04/
[30]: http://www.vagrantup.com/
[40]: https://github.com/airbnb/airflow
[50]: http://nerds.airbnb.com/airflow/

There are [Puppet][60] scripts that automatically install the software when the VM is started.

[60]: http://puppetlabs.com/

## Connect to the VM

1. To start the virtual machine(VM) type

    ```
    vagrant up airflow-local
    ```

2. Connect to the VM

    ```
    vagrant ssh airflow-local
    ```

## Initialize Airflow

1. Setup the home directory

    ```
    export AIRFLOW_HOME=~/airflow
    ```

2. Initialize the sqlite database

    ```
    airflow initdb
    ```

3. Start the web server

    ```
    airflow webserver -p 8080
    ```

4. Open a web browser to the UI at http://192.168.33.10:8080

## Run a task

1. List DAGS

    ```
    airflow list_dags
    ```

2. List tasks for `example_bash_operator` DAG

    ```
    airflow list_tasks example_bash_operator
    ```

3. List tasks for `example_bash_operator` in a tree view

    ```
    airflow list_tasks example_bash_operator -t
    ```

4. Run the `runme_0` task on the `example_bash_operator` DAG today

    ```
    airflow run example_bash_operator runme_0 `date +%Y-%m-%d`
    ```

## Documentation

1. Main documentation

    * https://pythonhosted.org/airflow/

2. Videos on Airflow

    * https://www.youtube.com/watch?v=dgaoqOZlvEA&feature=youtu.be

2. Slides

    * http://www.slideshare.net/walterliu7/airflow-a-data-flow-engine
    * http://www.slideshare.net/Hadoop_Summit/airflow-an-open-source-platform-to-author-and-monitor-data-pipelines

4. Airflow reviews

    * http://bytepawn.com/airflow.html
    * https://www.pandastrike.com/posts/20150914-airflow

## Disable logging

1. Change to the airflow directory

    ```
    cd /vagrant/airflow
    ```

2. Set airflow environment

    ```
    source set_airflow_env.sh
    ```

3. Run airflow without any logging messages

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
