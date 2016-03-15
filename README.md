# discovery-python

Programmatically find service endpoints.

This library currently is just an abstraction around reading environment variables used for dependent services.

## Installation

### pip

```sh
pip install git+https://<clever-drone Github token>@github.com/Clever/discovery-python.git@<version_tag>
```

The Github token can be found in [dev-passwords](https://github.com/Clever/clever-ops/tree/master/credentials).

### setup.py

```python
from setuptools import setup

# Assuming discovery v0.1.0 is being installed:
setup(

    # ...

    install_requires=['discovery==0.1.0'],
    dependency_links=[
      'https://<clever-drone Github token>@github.com/Clever/discovery-python/tarball/v0.1.0#egg=discovery-0.1.0'
    ],

    # ...

)
```

The Github token can be found in [dev-passwords](https://github.com/Clever/clever-ops/tree/master/credentials).

## Usage

```python
import discovery

try:
	redis_url = discovery.url('stoked', 'thrift')

	redis_host_and_port = discovery.host_port('stoked', 'thrift')

	redis_host = discovery.host('stoked', 'thrift')

	redis_port = discovery.port('stoked', 'thrift')

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
SERVICE_REDIS_TCP_PROTO = "tcp"
SERVICE_REDIS_TCP_HOST = "localhost"
SERVICE_REDIS_TCP_PORT = "6379"
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
