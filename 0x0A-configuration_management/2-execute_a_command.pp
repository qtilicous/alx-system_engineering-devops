# Puppet manifest to kill a process named killmenow using pkill

exec { 'killmenow_process':
  command => '/usr/bin/pkill -f killmenow',
  onlyif  => '/usr/bin/pgrep -f killmenow',
}
