#!/usr/bin/env bash
# Ensure the SSH client configuration file exists

file { '/home/ubuntu/.ssh/config':
  ensure => present,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0600',
}

# Configure SSH client to use the private key ~/.ssh/school
file_line { 'Declare identity file':
  path   => '/home/ubuntu/.ssh/config',
  line   => '    IdentityFile ~/.ssh/school',
  ensure => present,
}

# Configure SSH client to refuse password authentication
file_line { 'Turn off passwd auth':
  path   => '/home/ubuntu/.ssh/config',
  line   => '    PasswordAuthentication no',
  ensure => present,
}
