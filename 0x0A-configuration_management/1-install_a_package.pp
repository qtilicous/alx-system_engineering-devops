# Puppet manifest to install Flask from pip3

exec { 'install_flask':
  command  => 'pip3 install Flask==2.1.0',
  path     => ['/usr/bin'],
  provider => shell,
  require  => Package['python3-pip'], # Ensure pip3 is installed first
}

package { 'python3-pip':
  ensure => installed,
}
