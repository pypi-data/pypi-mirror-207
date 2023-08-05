# PyProton

[![PyPI version](https://badge.fury.io/py/pyproton.svg)](https://badge.fury.io/py/pyproton)

This package is a lightweight minimal wrapper implementation of the linux protonvpn-cli; designed to be an intuitive and simple to use interface for the Proton VPN in python.

## Getting Started

### **Install the CLI:**

[Proton VPN Docs](https://protonvpn.com/support/linux-vpn-tool/)

Debian based distros
1. [Download the Proton VPN DEB package](https://repo.protonvpn.com/debian/dists/stable/main/binary-all/protonvpn-stable-release_1.0.3_all.deb)
2. Install the Proton VPN repository
   
   `sudo apt-get install {/path/to/}protonvpn-stable-release_1.0.3_all.deb`
3. Update the apt-get package list
   
   `sudo apt-get update`
4. Install the Proton VPN Linux CLI
   
   `sudo apt-get install protonvpn-cli` 

### **Install pyproton:**

`pip install pyproton`

### **Import and use pyproton VPN:**

#### Args

* `user` **required:** user name string
* `pw` **required:** password string
* `verbose` **optional:** (`default=False`) turns on/off the stdin output for each step.
* `retries` **optional:** (`default=3`) defines number of retries when VPN connection times out.
* `timeout` **optional:** (`default=20`) seconds to wait before timing out a login attempt.

#### Methods

* `vpn.login()` log the user into proton VPN - (context manager): `__enter__`
* `vpn.logout()` log the user out of proton VPN - (context manager): `__exit__`
* `vpn.connect()` connect to proton VPN endpoint - (context manager): `__enter__`
* `vpn.disconnect()` disconnect from proton VPN endpoint - (context manager): `__exit__`
* `vpn.shuffle()` disconnects from the current VPN and connected to another

**NOTE:** It is generally recommended to use `dotenv` or some secrets library to load in credentials.

```python
import os
from pyproton import VPN

user = 'user'
pw = 'pw'

with VPN(user, pw) as vpn:
    print('do some stuff')
    vpn.shuffle()
    print('do more stuff')
```

### **TO-DO**

* PyTest & Tox testing
* Sphynx docs
* Coverage
* Deepsource scanning