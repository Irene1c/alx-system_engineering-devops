# client SSH configuration

file_line { 'password_authentication':
  path   => '/etc/ssh/ssh_config',
  line   => '	PasswordAuthentication no',
}

file_line { 'identity_file':
  path   => '/etc/ssh/ssh_config',
  line   => '	IdentityFile ~/.ssh/school',
}
