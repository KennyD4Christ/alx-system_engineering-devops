# This Puppet manifest ensures the correct ownership and permissions for /var/www/html/index.php and restarts Apache if necessary.

file { '/var/www/html/index.php':
  ensure => file,
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0644',
}

exec { 'restart_apache':
  command     => '/usr/sbin/service apache2 restart',
  refreshonly => true,
  subscribe   => File['/var/www/html/index.php'],
}
