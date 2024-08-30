import kayvee.logger as logger
import os


_SERVICE_ENV_VAR_TEMPLATE = 'SERVICE_{service_name}_{expose}_{component}'
_EXTERNAL_ENV_VAR_TEMPLATE = 'EXTERNAL_URL_{url}'


def url(service_name, expose):
  """
  Returns the URL for the given service and exposed interface, based on
  environment variables of the form
  `SERVICE_{SERVICE NAME}_{EXPOSE}_{PROTO|HOST|PORT}`.
  """
  return '{}://{}'.format(proto(service_name, expose), host_port(service_name, expose))


def host_port(service_name, expose):
  """
  Returns a `{HOST}:{PORT}` string for the given service and exposed interface,
  based on environment variables of the form
  `SERVICE_{SERVICE NAME}_{EXPOSE}_{HOST|PORT}`.
  """
  return '{}:{}'.format(host(service_name, expose), port(service_name, expose))


def host(service_name, expose):
  """
  Returns the host name for the given service and exposed interface, based on
  environment variables of the form `SERVICE_{SERVICE NAME}_{EXPOSE}_{HOST}`.
  """
  return _get_service_env_var(service_name, expose, 'HOST')


def port(service_name, expose):
  """
  Returns the port for the given service and exposed interface, based on
  environment variables of the form `SERVICE_{SERVICE NAME}_{EXPOSE}_{PROTO}`.
  """
  return _get_service_env_var(service_name, expose, 'PORT')


def proto(service_name, expose):
  """
  Returns the protocol for the given service and exposed interface, based on
  environment variables of the form `SERVICE_{SERVICE NAME}_{EXPOSE}_{PROTO}`.
  """
  return _get_service_env_var(service_name, expose, 'PROTO')

def external_url(url):
  """
  Returns the url for external based on environment variables of the form `EXTERNAL_URL_{URL}`.
  """
  return _get_external_env_var(url)

def _get_env_var(var_name):
  value = os.environ.get(var_name)
  if (value is None):
    raise MissingEnvironmentVariableError(var_name)
  return value

def _get_service_env_var(service_name, expose, component):
  var_name = _SERVICE_ENV_VAR_TEMPLATE.format(
      service_name=service_name, expose=expose, component=component)
  var_name = var_name.upper().replace('-', '_')

  return _get_env_var(var_name)

def _get_external_env_var(url):
  var_name = _EXTERNAL_ENV_VAR_TEMPLATE.format(url=url)
  var_name = var_name.upper().replace('.', '_')

  return _get_env_var(var_name)


class MissingEnvironmentVariableError(Exception):

  """Raised when a required environment cannot be found."""

  def __init__(self, var_name):
    self.var_name = var_name

  def __str__(self):
    return 'Missing environment variable `{}`.'.format(self.var_name)
