# Puppet manifest to configure custom HTTP header response

# Define class for configuring custom HTTP header
class custom_http_response_header {

  # Install facter for hostname fact
  package { 'facter':
    ensure => installed,
  }

  # Define exec resource to get the hostname
  exec { 'get_hostname':
    command => '/usr/bin/facter hostname',
    path    => ['/bin', '/usr/bin'],
    # Define a custom fact to store the hostname
    environment => ["FACTER_hostname=$hostname"],
    # Notify Nginx service to restart if hostname changes
    notify  => Service['nginx'],
    # Only refresh if the hostname changes
    refreshonly => true,
  }

  # Define file resource to add custom HTTP header in Nginx configuration
  file { '/etc/nginx/sites-available/default':
    ensure  => present,
    content => template('nginx/default.erb'),
    # Notify Nginx service to restart if configuration changes
    notify  => Service['nginx'],
  }
}

# Include the custom_http_response_header class
include custom_http_response_header
