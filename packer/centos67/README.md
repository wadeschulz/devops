Usage
-----

* Download [Packer](https://www.packer.io/downloads.html)

* Updated version uses command line params (or config file) to pass server info to packer

* `packer build -var 'ESXI_IP=...' -var 'ESXI_USER=...' -var 'ESXI_PASS=...' ubuntu-1404.json`

* Register and start VM (ssh into ESXi)
 - `vim-cmd solo/registervm /vmfs/volumes/datastore1/output-vmware-iso/packer-vmware-iso.vmx`
 - `vim-cmd vmsvc/getallvms` - locate Vmid
 - `vim-cmd vmsvc/power.on {{Vmid}}`