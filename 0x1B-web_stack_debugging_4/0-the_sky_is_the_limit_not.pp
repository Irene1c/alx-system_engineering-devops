# Updating operating systems file descriptor limit
# Modify ulimit in the /etc/default/nginx file

file { '/etc/default/nginx':
  ensure  => file,
  content => 'ULIMIT="-n 3072"',
}

# Restart Nginx
exec { 'restart_nginx':
  command => '/usr/sbin/service nginx restart',
}
