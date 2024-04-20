# Define variable for key path (if not directly specified in the template)
$key_path = '/home/kennyd/.ssh/school'

file { '/etc/ssh/sshd_config':
  ensure  => present,
  content => template('/home/kennyd/alx-system_engineering-devops/0x0B-ssh/templates/sshd_config.erb'),
}
