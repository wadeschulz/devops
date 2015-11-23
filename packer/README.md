Usage
-----

* Download [Packer](https://www.packer.io/downloads.html)

* Updated version uses command line params (or config file) to pass server info to packer

* `packer build -var 'ESXI_IP=...' -var 'ESXI_USER=...' -var 'ESXI_PASS=...' -var 'VM_NAME=...' -var 'DATASTORE=...' ubuntu-1404.json`

* Register and start VM (ssh into ESXi)
 - `vim-cmd solo/registervm /vmfs/volumes/{DATASTORE}/output-{NAME}/packer-{NAME}.vmx`
 - `vim-cmd vmsvc/getallvms` - locate Vmid
 - `vim-cmd vmsvc/power.on {{Vmid}}`
