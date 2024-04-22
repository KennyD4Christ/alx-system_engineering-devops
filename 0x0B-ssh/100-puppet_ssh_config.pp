# Define variable for key path (if not directly specified in the template)
file { '/home/kennyd/.ssh/config':
  ensure  => present,
  mode    => '0600',
  owner   => 'kennyd',
  group   => 'kennyd',
  content => "Host my_server\n  HostName 100.26.122.117\n  IdentityFile ~/.ssh/school\n  PasswordAuthentication no\n",
}
