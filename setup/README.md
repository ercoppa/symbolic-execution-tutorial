# Setup for VM BIAR 1.6.5

## Download the VM (no need in the lab!)

The OVA file of the VM can be downloaded using this [link](https://drive.google.com/drive/u/0/search?q=LXLE-BIAR-1.6.5.ova). The OVA file can be imported using VirtualBox.

## Install angr
```
./setup/install-angr.sh
```

## Download and install IDA Freeware Linux

(it takes a few minutes since the binary is 45MB)
```
./setup/install-IDA.sh
```
Follow the instructions from the setup wizard. Install it in the default location.

## Run IDA Freeware Linux

```
./setup/run-IDA.sh
```