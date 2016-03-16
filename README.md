# discovery-python

Programmatically find service endpoints.

This library currently is just an abstraction around reading environment variables used for dependent services.

## Installation

### pip

Assuming discovery v0.1.0 is being installed:

```sh
pip install git+ssh://github.com/Clever/discovery-python.git@v0.1.0
```

### setup.py

```python
from setuptools import setup

GITHUB_TOKEN = os.environ['GITHUB_API_TOKEN']

# Assuming discovery v0.1.0 is being installed:
setup(

    # ...

    install_requires=['discovery==0.1.0'],
    dependency_links=[
      'https://{}@github.com/Clever/discovery-python/tarball/v0.1.0#egg=discovery-0.1.0'.format(GITHUB_TOKEN)
    ],

    # ...

)
```

## Usage

```python
import discovery

try:
	stoked_url = discovery.url('stoked', 'thrift')

	stoked_host_and_port = discovery.host_port('stoked', 'thrift')

	stoked_host = discovery.host('stoked', 'thrift')

	stoked_port = discovery.port('stoked', 'thrift')

except discovery.MissingEnvironmentVariableError as e:
	print 'ERROR: Stoked discovery failed: {}.'.format(e)

```

## Environment Variables

This library currently requires environment variables to be defined in the following format:

```
SERVICE_{SERVICE_NAME}_{EXPOSE}_{PROTO|HOST|PORT}
```

### Example:
```bash
SERVICE_STOKED_THRIFT_PROTO = "tcp"
SERVICE_STOKED_THRIFT_HOST = "localhost"
SERVICE_STOKED_THRIFT_PORT = "90"
```

## Development

### Publishing a new version

1. Bump the version in the `VERSION` file and update the changelog in `CHANGES.md`.
2. Merge your changes into `master`.
3. Checkout `master`
4. Run the publish script:

    ```sh
    ./publish.sh
    ```
