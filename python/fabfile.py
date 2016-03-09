from __future__ import print_function
from fabric.api import run, env, task, roles, local, lcd, hide
from gitric.api import git_seed, git_reset

import os
import datetime

script_dir = os.path.dirname(__file__)


# env.roledefs['master'] = config['master']
# env.roledefs['workers'] = config['workers']
# env.use_ssh_config = True

INSTANCE_TYPE = 'm3.xlarge'


@task(name='hostname')
def hostname():
    ' display name of host '
    local('hostname')


@task(name='sph')
def spot_price_history(inst_type=INSTANCE_TYPE, region='us-west-2'):
    ' spot price history '
    now = datetime.datetime.utcnow()
    start_time = '{:%Y-%m-%dT%H:00:00}'.format(now)
    aws_cmd = 'aws ec2 describe-spot-price-history --start-time {} --product "Linux/UNIX" --instance-type "{}"'
    aws_cmd = aws_cmd.format(start_time, inst_type)
    jq_cmd = 'jq -c -C ".SpotPriceHistory[] | {SpotPrice, AvailabilityZone, InstanceType }"'

    with hide("running"):
        os.environ['AWS_DEFAULT_REGION'] = region
        local('|'.join([aws_cmd, jq_cmd]))


@task
def dt():
    ' get current datetime '
    now = datetime.datetime.utcnow()
    print('{:%Y-%m-%dT%H:00:00}'.format(now))


@task
def regions():
    ' get list of regions '
    aws_cmd = 'aws ec2 describe-regions'
    jq_cmd = 'jq -c -C ".Regions[]"'
    with hide("running"):
        local('|'.join([aws_cmd, jq_cmd]))


@task(name='ri')
def run_instances():
    ' run instances '
    aws_cmd = 'aws ec2 run-instances --image-id ami-9abea4fb --count 1 --instance-type m3.medium --key-name ubuntu_trusty --security-group-ids ssh-ip-only'

    jq_cmd = 'jq -c -C "."'
    with hide("running"):
        local('|'.join([aws_cmd, jq_cmd]))


@task(name='rsi')
def request_spot_instances(
        price=0.01, zone='us-west-2a', inst_type=INSTANCE_TYPE,
        inst_id="ami-9abea4fb"):
    ' request spot instances '
    # ami-9abea4fb - ubuntu-trusty-14.04-amd64-server
    launch_specification = '''
        {{
          "ImageId": "{}",
          "KeyName": "ubuntu_trusty",
          "SecurityGroupIds": [ "sg-94a671f3" ],
          "InstanceType": "{}"
        }}
    '''.format(inst_id, inst_type)
    ls_encode = launch_specification.replace('\n', '')
    ls_encode = ls_encode.replace('"', '\\"')
    aws_cmd = 'aws ec2 request-spot-instances --spot-price "{}" --instance-count 1 --type "one-time" --availability-zone-group {} --launch-specification "{}"'
    aws_cmd = aws_cmd.format(price, zone, ls_encode)
    jq_cmd = 'jq -c -C "."'
    with hide("running"):
        local('|'.join([aws_cmd, jq_cmd]))


@task(name='di')
def describe_instances():
    ' describe instances '
    aws_cmd = 'aws ec2 describe-instances'
    jq_cmd = 'jq -c -C ".Reservations[].Instances[]| {InstanceType, KeyName, State: .State.Name, PublicIpAddress, InstanceId, ImageId}"'
    with hide("running"):
        local('|'.join([aws_cmd, jq_cmd]))


@task(name='dsir')
def describe_spot_instance_requests():
    ' describe spot instance requests '
    # aws_cmd = 'aws ec2 describe-spot-instance-requests --query "SpotInstanceRequests[].{Status:Status, SpotPrice:SpotPrice}"'
    aws_cmd = 'aws ec2 describe-spot-instance-requests'
    jq_cmd = 'jq -c -C ".SpotInstanceRequests[] | {Code:.Status.Code, SpotPrice, RequestId:.SpotInstanceRequestId}"'
    with hide("running"):
        local('|'.join([aws_cmd, jq_cmd]))


@task(name='csir')
def cancel_spot_instance_requests(request_id):
    ' cancel spot instance requests '
    aws_cmd = 'aws ec2 cancel-spot-instance-requests --spot-instance-request-ids {}'.format(request_id)
    jq_cmd = 'jq -c -C ".CancelledSpotInstanceRequests[] | {State, RequestId:.SpotInstanceRequestId}"'

    with hide("running"):
        local('|'.join([aws_cmd, jq_cmd]))
        # local(aws_cmd)


@task(name='ti')
def terminate_instances(inst_id):
    ' terminate instances '
    aws_cmd = 'aws ec2 terminate-instances --instance-ids {}'
    aws_cmd = aws_cmd.format(inst_id)
    with hide("running"):
        local(aws_cmd)


@task
def storm_add(ip):
    ' add to ssh config '
    cmd = 'storm add --id_file ~/ubuntu_trusty.pem aws ubuntu@{}'
    cmd = cmd.format(ip)
    with hide("running"):
        local(cmd)


@task
def storm_list():
    ' list ssh config '
    cmd = 'storm list'
    with hide("running"):
        local(cmd)


@task
def storm_delete(name):
    ' delete ssh config by name '
    cmd = 'storm delete {}'.format(name)
    with hide("running"):
        local(cmd)


@task(name='dim')
def describe_images():
    ' describe images owned by self '
    aws_cmd = 'aws ec2 describe-images --owners self'
    jq_cmd = 'jq -c -C ".Images[] | {Name, ImageId, Description}"'
    with hide("running"):
        local('|'.join([aws_cmd, jq_cmd]))

#  aws ec2 describe-images --owners self
