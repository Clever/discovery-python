import discovery
import os
import unittest

from discovery import MissingEnvironmentVariableError


class TestDiscovery(unittest.TestCase):

  def test_host_available(self):
    host = 'host-available.ops.clever.com'
    os.environ['SERVICE_HOST_AVAILABLE_TCP_HOST'] = host

    self.assertEqual(discovery.host('host-available', 'tcp'), host)

  def test_host_missing(self):
    with self.assertRaisesRegexp(MissingEnvironmentVariableError, 'SERVICE_HOST_MISSING_HTTP_HOST'):
      discovery.host('host-missing', 'http')

  def test_port_available(self):
    port = '5000'
    os.environ['SERVICE_PORT_AVAILABLE_TCP_PORT'] = port

    self.assertEqual(discovery.port('port-available', 'tcp'), port)

  def test_port_missing(self):
    with self.assertRaisesRegexp(MissingEnvironmentVariableError, 'SERVICE_PORT_MISSING_HTTP_PORT'):
      discovery.port('port-missing', 'http')

  def test_proto_available(self):
    proto = 'http'
    os.environ['SERVICE_PROTO_AVAILABLE_TCP_PROTO'] = proto

    self.assertEqual(discovery.proto('proto-available', 'tcp'), proto)

  def test_proto_missing(self):
    with self.assertRaisesRegexp(
            MissingEnvironmentVariableError, 'SERVICE_PROTO_MISSING_HTTP_PROTO'):
      discovery.proto('proto-missing', 'http')

  def test_host_port_available(self):
    host = 'host-port-available.ops.clever.com'
    os.environ['SERVICE_HOST_PORT_AVAILABLE_HTTP_HOST'] = host

    port = '5000'
    os.environ['SERVICE_HOST_PORT_AVAILABLE_HTTP_PORT'] = port

    self.assertEqual(discovery.host_port('host-port-available', 'http'), '{}:{}'.format(host, port))

  def test_host_port_missing_port(self):
    host = 'port-missing.ops.clever.com'
    os.environ['SERVICE_PORT_MISSING_HTTP_HOST'] = host

    with self.assertRaisesRegexp(MissingEnvironmentVariableError, 'SERVICE_PORT_MISSING_HTTP_PORT'):
      discovery.host_port('port-missing', 'http')

  def test_url_available(self):
    proto = 'http'
    os.environ['SERVICE_URL_AVAILABLE_BLAH_PROTO'] = proto

    host = 'user:pasws@url-available.ops.clever.com'
    os.environ['SERVICE_URL_AVAILABLE_BLAH_HOST'] = host

    port = '9090'
    os.environ['SERVICE_URL_AVAILABLE_BLAH_PORT'] = port

    self.assertEqual(discovery.url('url-available', 'blah'), '{}://{}:{}'.format(proto, host, port))

  def test_url_missing_host(self):
    proto = 'tcp'
    os.environ['SERVICE_PROTO_MISSING_TCP_PROTO'] = proto

    port = '9090'
    os.environ['SERVICE_PROTO_MISSING_TCP_PORT'] = port

    with self.assertRaisesRegexp(MissingEnvironmentVariableError, 'SERVICE_PROTO_MISSING_TCP_HOST'):
      discovery.url('proto-missing', 'tcp')
