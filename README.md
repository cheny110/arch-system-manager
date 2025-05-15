# Arch System Manager

A lightweight tool for managing and automating system tasks on Arch Linux.

## Features

- Package installation and removal
- System updates
- Service management
- Custom script execution

## Requirements

- Arch Linux or compatible distribution
- Bash 5.0+
- `sudo` privileges

## Installation

```bash
git clone https://github.com/yourusername/arch-system-manager.git
uv --directory [Path]  run server.py
```

## Usage

```bash
uv --directory [Path]  run server.py
```

### Options

- `install <package>`: Install a package
- `remove <package>`: Remove a package
- `update`: Update system packages
- `service <name> <start|stop|restart>`: Manage services

## Contributing

Pull requests are welcome. For major changes, please open an issue first.

## License

[MIT](LICENSE)