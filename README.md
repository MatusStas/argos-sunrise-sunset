# Sunrise & Sunset

This extension is created specially for [Argos GNOME Shell extension](https://github.com/p-e-w/argos). It shows in top bar sunrise and sunset for current date. When extension is connected to the internet, it downloads all data for the rest of the month and saves it into `data.plk`. If there is no internet connection and no downloaded data available, it shows in top bar *offline and no data available*.

![extension_wifi](img/data_available.png)

downloaded data available

![extension_no_wifi](img/no_data_available.png)

no internet connection and no downloaded data available

## Installing

* add [GNOME Shell integration
](https://chrome.google.com/webstore/detail/gnome-shell-integration/gphhapmejobijbbhgpjhcjognlahblep?hl=en) to google chrome extensions
* install [Argos extension](https://extensions.gnome.org/extension/1176/argos/)


## Setting up `config.py`


```python
LATITUDE = "LATITUDE"
LONGITUDE = "LONGITUDE"
DATA_PATH = "/FULL/PATH/TO/data.plk"
```

## Setting up `sunrise-sunset.1s.sh`

```bash
#!/bin/bash

data=$(python3 /FULL/PATH/TO/main.py)
echo $data
```

* make `sunrise-sunset.1s.sh` executable
* move to `.config.argos/`
* enjoy