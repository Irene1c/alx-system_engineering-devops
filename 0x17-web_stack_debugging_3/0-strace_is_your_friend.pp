# puppet manifest to modify wp-settings.php file
# the path attribute shows puppet where to find the sed command

exec { 'modify_wp_settings_line':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/usr/bin', '/bin'],
}
