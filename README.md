# MullvadAPI

Python wrapper around Mullvad api

## Installation

```bash
pip install mullvad_api
```

## QuickStart

```python
>>> from mullvad_api import MullvadAPI
>>> mullvad = MullvadAPI()
>>> mullvad.data.keys()             # List Mullvad API keys
>>> mullvad.data["mullvad_exit_ip"] # Check if Mullvad VPN is active
True
>>> mullvad.data["ip"]              # Check exit ip address
'89.46.62.92'
```
