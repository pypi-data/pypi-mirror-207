# DNS Manager For ArvanCloud

## Installation

```bash
pip install arvan-dns
```

## Usage

### create a text file with your domains

```txt
example.com
example.ir
example.net
```

### run the command

```bash
arvan-dns --bearer_token=<your bearer_token> --old_ip=<your old ip> --new_ip=<your new ip> --domains_file=<your domains file>
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
