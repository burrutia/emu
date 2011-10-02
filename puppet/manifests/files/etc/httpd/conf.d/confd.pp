class gitservr_ht_cnfd
{
  file {"/etc/httpd/conf.d":
  owner => "root",
  group => "root",
  purge => true,
  recurse => true,
  force => true,
  source => "puppet:///files/git/etc/httpd/conf.d"
  }
}

class config_null
{
 include null_pxy_ajp
 include null_ssl_cnf 
 include null_php_cnf 
 include null_wcnf 
}

class nagios_nullconf
{
 include null_pxy_ajp
 include null_wconf 
}

class null_pxy_ajp { file {"/etc/httpd/conf.d/proxy_ajp.conf": ensure=> absent } }
class null_ssl_cnf { file {"/etc/httpd/conf.d/ssl.conf": ensure=> absent } }
class null_php_cnf { file {"/etc/httpd/conf.d/php.conf": ensure=> absent } }
class null_wconf { file {"/etc/httpd/conf.d/welcome.conf": ensure=> absent } }



class nagios_conf
{
 file { "/etc/httpd/conf.d/nagios.conf":
  owner => "root",
  group => "root",
  mode => "0644",
  notify => Service[httpd],
  content => template("/etc/puppet/manifests/templates/mon/etc/httpd/conf.d/nagios.conf")
  }
}


class nagios_php_conf
{
 file { "/etc/httpd/conf.d/php.conf":
  owner => "root",
  group => "root",
  mode => "0644",
  notify => Service[httpd],
  content => template("/etc/puppet/manifests/templates/mon/etc/httpd/conf.d/php.conf")
  }
}

class nagios_ssl_conf
{
 file { "/etc/httpd/conf.d/ssl.conf":
  owner => "root",
  group => "root",
  mode => "0644",
  notify => Service[httpd],
  content => template("/etc/puppet/manifests/templates/mon/etc/httpd/conf.d/nagios-ssl.conf")
   }
}

