# Configgy

A subtle Python package for loading configuration files without having to specify the file type.

## Installation

You can install the package from PyPI using pip:

```bash
pip install configgy
```

## Usage

Here's an example of how to use the package to load a configuration file:

```python
from configgy.loader import ConfigLoader

data = ConfigLoader().load_config_file("file.json")
```

The `load_config` function takes a single argument, the path to the configuration file. It will automatically detect the file type and use the appropriate loader.

Currently, the package supports the following file types:

- INI
- YAML
- TOML
- JSON
