class web_elb_fwall
{
   include iptables
   file { "/etc/sysconfig/iptables":
   owner => "root",
   group => "root",
   mode => 0644,
   notify => Service["iptables"],
   content => template("/etc/puppet/manifests/templates/web/etc/sysconfig/iptables")
   }
}
