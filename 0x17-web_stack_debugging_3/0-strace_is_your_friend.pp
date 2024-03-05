# Puppet manifest to fix Apache 500 error using strace

# Ensure Apache service is running
service { 'apache2':
  ensure => running,
}

# Ensure the correct permissions for the Apache log directory
file { '/var/log/apache2':
  ensure => directory,
  owner  => 'www-data',
  group  => 'www-data',
}

# Ensure the correct permissions for the Apache log files
file { '/var/log/apache2/error.log':
  ensure => file,
  owner  => 'www-data',
  group  => 'www-data',
}

# Ensure the correct permissions for the Apache PID file
file { '/var/run/apache2/apache2.pid':
  ensure => file,
  owner  => 'www-data',
  group  => 'www-data',
}

# Ensure the correct permissions for the Apache configuration directory
file { '/etc/apache2/':
  ensure => directory,
  owner  => 'root',
  group  => 'root',
}

# Ensure the correct permissions for the Apache configuration file
file { '/etc/apache2/apache2.conf':
  ensure => file,
  owner  => 'root',
  group  => 'root',
}

# Ensure the correct permissions for the Apache sites-available directory
file { '/etc/apache2/sites-available/':
  ensure => directory,
  owner  => 'root',
  group  => 'root',
}

# Ensure the correct permissions for the Apache sites-enabled directory
file { '/etc/apache2/sites-enabled/':
  ensure => directory,
  owner  => 'root',
  group  => 'root',
}

# Ensure the correct permissions for the Apache default site configuration file
file { '/etc/apache2/sites-available/000-default.conf':
  ensure => file,
  owner  => 'root',
  group  => 'root',
}
