Usage
-----

* Download [Packer](https://www.packer.io/downloads.html)

* Export environment variables
 - `export ESXI_PASSWORD=...`
 - `export ESXI_IP=...`

* `packer build ubuntu-1404.json`

* Register and start VM (ssh into ESXi)
 - `vim-cmd solo/registervm /vmfs/volumes/datastore1/output-vmware-iso/packer-vmware-iso.vmx`
 - `vim-cmd vmsvc/getallvms` - locate Vmid
 - `vim-cmd vmsvc/power.on {{Vmid}}`
