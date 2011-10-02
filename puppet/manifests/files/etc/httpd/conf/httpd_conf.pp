class gitweb_httpd_conf
{
 file { "/etc/httpd/conf/httpd.conf":
  owner => "root",
  group => "root",
  mode => "0644",
  content => template("/etc/puppet/manifests/templates/git/etc/httpd/conf/httpd.conf")
  }
}

class mon_httpd_conf
{
 file { "/etc/httpd/conf/httpd.conf":
  owner => "root",
  group => "root",
  mode => "0644",
  notify => Service[httpd],
  content => template("/etc/puppet/manifests/templates/mon/etc/httpd/conf/httpd.conf")
  }
}

class nagios_httpd_conf
{
 file { "/etc/httpd/conf/httpd.conf":
  owner => "root",
  group => "root",
  mode => "0644",
  notify => Service[httpd],
  content => template("/etc/puppet/manifests/templates/mon/etc/httpd/conf/nagios-httpd.conf")
  }
}
