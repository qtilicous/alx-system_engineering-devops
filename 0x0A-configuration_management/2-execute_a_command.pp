# Puppet manifest to kill a process named killmenow using pkill

exec { 'killmenow_process':
  command => 'pkill -f killmenow',
  onlyif  => 'pgrep -f killmenow',
}
