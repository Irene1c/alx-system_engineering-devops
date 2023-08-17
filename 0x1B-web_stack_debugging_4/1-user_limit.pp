# Update the resource limits for the 'holberton' user

exec {'update_holberton_hard_nofile_limits':
  command => "sed -i 's/holberton hard nofile 5/holberton hard nofile 1000/' /etc/security/limits.conf",
  path    => ['/bin', '/usr/bin'],
}

exec {'update_holberton_soft_nofile_limits':
  command => "sed -i 's/holberton soft nofile 4/holberton soft nofile 1000/' /etc/security/limits.conf",
  path    => ['/bin', '/usr/bin'],
}
