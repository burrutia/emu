# php_ini

class php_default_ini
{
  file { "/etc/php.ini":
   owner => 'root',
   group => 'root',
   mode => 0644,
   content => template("/etc/puppet/manifests/templates/web/etc/php_default.ini")
   } 
}

class php_dev_ini
{
  file { "/etc/php.ini":
  ensure => link,
  target => '/home/web_user/php.ini'
  }
}
