# mutil

Utilities for managing memory resources with cgroups

Memory management is an important consideration for a multi-user computing server, because if users collectively attempt to use more memory than is available on the system, it may crash. A useful means of preventing this is [cgroups](https://manpages.ubuntu.com/manpages/focal/man7/cgroups.7.html) which can assign users to "control groups" which are limited to a given quantity of resources (such as CPU, disk, or memory usage).

However, `cgroups` are somewhat complicated to use in practice. `mutil` streamlines the memory management component.

## Installation

To install `mutil`:
```sh
conda create -c conda-forge -n mutil psutil
conda activate mutil
pip install mutil
```

You may wish to include `mutil` and `nvtop` in one environment:
```sh
conda create -c conda-forge -n mutil-nvtop psutil nvtop
conda activate mutil-nvtop
pip install mutil
```

You can also install it in an existing environment by simply using `pip install mutil`. Then you can check it with:

```sh
mutil --version
mutil --help
```

`mutil` maintains 

Induct a user

```sh
mutil induct -u <username>
```

Check your memory usage

```sh
mutil usage
```

Check usage of another user

```sh
mutil usage -u <username>
```

Check usage of a group

```sh
mutil usage -g free
```
