# Define variable for key path (if not directly specified in the template)

file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/home/kennyd/.ssh/config',
  line   => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  ensure => present,
  path   => '/home/kennyd/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
}

file_line { 'Add server configuration':
  ensure => present,
  path   => '/home/kennyd/.ssh/config',
  line   => 'Host my_server',
}

file_line { 'Add server IP':
  ensure => present,
  path   => '/home/kennyd/.ssh/config',
  line   => '  HostName 100.26.122.117',
}
