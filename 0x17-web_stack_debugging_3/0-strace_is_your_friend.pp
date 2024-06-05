# fixes bad "phpp" extensions to "php" in "wp-settings.php".

exec{'fix-wordpress':
  command => 'sed -i a/phpp/php/g /var/www/htlm/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
