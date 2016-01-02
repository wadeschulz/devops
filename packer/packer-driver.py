import getpass
import os
from paramiko import SSHClient

build_type = raw_input('Enter build type (ubuntu1404, centos7, etc): ')
esxi_server = raw_input('ESXI server address: ')
esxi_username = raw_input('ESXI SSH username: ')
esxi_password = getpass.getpass('ESXI SSH password: ')
datastore = raw_input('Datastore name: ')
vm_base_name = raw_input('VM/Build name: ')
num_instances = int(raw_input('Number instances: '))

os.chdir(build_type)

for i in range(1, num_instances+1):
	vm_name = vm_base_name + "-" + str(i)
	packer_ip = " -var 'ESXI_IP=" + esxi_server + "'"
	packer_user = " -var 'ESXI_USER=" + esxi_username + "'"
	packer_pass = " -var 'ESXI_PASS=" + esxi_password + "'"
	packer_datastore = " -var 'DATASTORE=" + datastore + "'"
	packer_vm_name = " -var 'VM_NAME=" + vm_name + "'"

	os.system("/opt/packer/packer build" + packer_ip + packer_user + packer_pass + packer_datastore + packer_vm_name + " packer-config.json")

	ssh = SSHClient()
	ssh.load_system_host_keys()
	ssh.connect(esxi_server, username=esxi_username, password=esxi_password)

	register_vm = "vim-cmd solo/registervm /vmfs/volumes/" + datastore + "/output-" + vm_name + "/packer-" + vm_name + ".vmx"

	ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(register_vm)
