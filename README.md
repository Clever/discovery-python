# discovery-python

This library programmatically finds endpoints for dependencies. Similar to [discovery-go](https://github.com/Clever/discovery-go) and [disocvery-node](https://github.com/Clever/discovery-node).

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

## Development

### Publishing a new version

1. Bump the version in the `VERSION` file and update the changelog in `CHANGES.md`.
2. Merge your changes into `master`.
3. Checkout `master`
4. Run the publish script:

    ```sh
    ./publish.sh
    ```

### Implementation Details

Currently, `discovery-{go,node,python}` looks for environment variables with the following format:

```
SERVICE_{SERVICE_NAME}_{EXPOSE_NAME}_{PROTO,HOST,PORT}
```

These environment variables are autogenerated by [fab](http://github.com/Clever/fabulaws) and [catapult](http://github.com/Clever/catapult) during app deployment.  Three env-vars are created for each app listed in the `dependencies` section of caller's launch yaml.

For example, if an app lists `district-authorizations` as a dependency, fab and catapult will generate this env-vars triplet:

```bash
SERVICE_DISTRICT_AUTHORIZATIONS_HTTP_PROTO = "http"
SERVICE_DISTRICT_AUTHORIZATIONS_HTTP_HOST = "district-authorizations.ops.clever.com"
SERVICE_DISTRICT_AUTHORIZATIONS_HTTP_PORT = "80"
```
