# common cve packages for updates
# diff file so that high risk targets 
# can be looked at easily periodically
class cve_apr_centos
 {
    package { "apr-1.2.7-11.el5_6.5.x86_64":
    ensure => installed,
    }
 }

class cve_apr_redhat
 {
    package { "apr-1.2.7-11.el5_5.3.x86_64":
    ensure => installed,
    }
 }

class cve_apr {
 case $operatingsystem {
 "CentOS": { include cve_apr_centos }
 "RedHat": { include cve_apr_redhat }
  default: { fail("Your OS is not supported") }
  }
}
