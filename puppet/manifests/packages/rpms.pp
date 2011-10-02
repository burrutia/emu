class default_packages
{
 package { [ "sudo", "vim-enhanced", "ruby-shadow", "tar", "bzip2" ]:
  ensure => installed,
 }
}

class debug_tools 
{
 package { [ "ltrace","strace" ]:
  ensure => installed,
 }
}


class ganglia_gmond
{
 package { [ "ganglia-gmond"]:
  ensure => installed,
 }
 service { "gmond":
      ensure => running,
 }
}

class ganglia_web
{
 package { [ "ganglia-gmetad", "ganglia-web-3.1.7-1.noarch"]:
  ensure => installed,
 }
 service { "gmetad":
      ensure => running,
 }
}

class php52
{
 package {
 [
  "php-cli-5.2.13-3.rs.el5.x86_64",
  "php-mbstring-5.2.13-3.rs.el5.x86_64",
  "php-xmlrpc-5.2.13-3.rs.el5.x86_64",
  "php-pear-1.4.9-6.el5.noarch",
  "php-soap-5.2.13-3.rs.el5.x86_64",
  "php-pdo-5.2.13-3.rs.el5.x86_64",
  "php-5.2.13-3.rs.el5.x86_64",
  "php-mysql-5.2.13-3.rs.el5.x86_64",
  "php-xml-5.2.13-3.rs.el5.x86_64",
  "php-common-5.2.13-3.rs.el5.x86_64",
  "php-devel-5.2.13-3.rs.el5.x86_64",
  "php-pecl-memcache-2.2.3-3.3.rs.el5.php52.x86_64"
 ]:
  ensure => installed,
  }
}


class php52_extras
{
 package {
 [ "php-gd-5.2.13-3.rs.el5.x86_64",
  "php-mcrypt-5.2.13-1oakley.x86_64"
 ]:
  ensure => installed,
  }
}

class httpd_64
{
package { ["httpd.x86_64", "mod_ssl.x86_64"]:
  ensure => installed,
  }
  service { "httpd":
      ensure => running,
  }
}

class mysql-server 
{
 package { ["mysql-server-5.0.77-4.el5_6.6.x86_64"]:
  ensure => installed,
  }
  service { "mysqld":
      ensure => running,
  }
}

class mysql55
{
 package {
  [ "MySQL-client-5.5.11-1.rhel5.x86_64",
     "MySQL-server-5.5.11-1.rhel5.x86_64"
  ]:
  ensure => installed,
 }
  service { "mysql":
      ensure => running,
  }
}

class mysql5512
{
 package { 
  [ "MySQL-server-5.5.12-1.rhel5", "MySQL-client-5.5.12-1.rhel5"
   ]:
  ensure => installed,
 }
  service { "mysql":
      ensure => running,
  }
}

class ntp 
{
  package { ["ntp"]:
  ensure => installed,
  }
  service { "ntpd":
      ensure => running,
  }
}

class sendmail {
   package { ["sendmail"]:
   ensure => installed,
   }
   service { "sendmail":
   ensure => running,
   }
}
class ssh_server {
   package { ["openssh-server-4.3p2-72.el5_6.3.x86_64"]:
   ensure => installed,
   }
   service { "sshd":
   ensure => running,
   }
}

class tree {
  package { ["tree"]:
  ensure => installed,
 }
}

class lsof {
 package {"lsof":
  ensure => installed,
 }
}

class iptables {
  package {"iptables":
    ensure => installed,
  }
 service { "iptables":
    ensure => running,
 }
}

class memcache {
 package {"memcached.x86_64":
 ensure => installed,
  }
 service { "memcached":
    ensure => running,
 }
}

class replicache {
  package { "memcached-1.2.8-repcached-2.2-1.x86_64":
  }
  service { "memcached-repcached":
  ensure => running,
  }
}


class membase {
  package {"membase-server.x86_64":
  ensure => installed,
  }
}


class mod-perl {
  package {["mod_perl.x86_64"]:
  ensure => installed,
  }
}

class mod-python {
  package {["mod_python.x86_64"]:
  ensure => installed,
  }
}

class nscd {
  package {"nscd":
  ensure => installed,
  }
  service { "nscd":
  ensure => stopped,
  }
}

class nfsutils {
   package {"nfs-utils":
   ensure => installed,
   }
  service { "nfs":
   ensure => running,
  }
}

class squid {
  package {"squid.x86_64":
  ensure => installed,
  }
}

class rubygems {
  package {"rubygems.noarch":
  ensure => installed,
  }
}

class rdoc_tls {
  package {["ruby-rdoc.x86_64", "ruby-irb.x86_64"]:
  ensure => installed,
  }
}


class cronolog {
  package { "cronolog":
   ensure => installed,
   }
}

class portmap { 
  package {"portmap":
   ensure => installed,
  }
  service { "portmap":
   ensure => running,
  }
}

class syslog {
  package {"sysklogd":
   ensure => installed,
  }
  service { "syslog":
  ensure => running,
  }
}

class yum_updatesd {
  package { "yum-updatesd":
    ensure => installed,
    }
  service { "yum-updatesd":
      ensure=> stopped,
  }
}

class nagios_server {
   package { [ "nagios-www-3.2.3-1.x86_64", "nagios-plugins-1.4.15-1.x86_64", "nagios-check-multi-0.25-1.x86_64","nagios-3.2.3-1.x86_64"]:
      ensure=> installed,
   }
  service { "nagios":
    ensure => running,
  }
}


class nagios_plugins {
   package { "nagios-plugins-1.4.15-88.x86_64":
      ensure=> installed,
   }
}

class nrpe_tools {
   package {["nrpe", "nagios-common", "nagios-plugins-nrpe"]:
    ensure => installed,
    }
   service { "nrpe":
    ensure => running,
  }
}

class rightscale {
    package { ["rightscale"]:
    ensure => "purged",
    }
}

class haproxy
{
  package { "haproxy-1.4.15-1":
  ensure => installed,
  }
 service { "haproxy":
      ensure => running,
 }
}
