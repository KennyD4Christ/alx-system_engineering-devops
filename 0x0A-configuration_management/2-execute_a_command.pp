# This Puppet manifest kills the process named killmenow using pkill

exec { 'killmenow':
  command => '/usr/bin/pkill -f killmenow',
  path    => ['/usr/bin'],  # Optional: Explicitly define path to pkill
}
