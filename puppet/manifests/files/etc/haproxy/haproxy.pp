class haproxy_conf
{
  file { "/etc/haproxy/haproxy.cfg":
   owner => 'root',
   group => 'root',
   mode => '0644',
   notify => Service[haproxy],
   content => template("/etc/puppet/manifests/class/vlb/etc/haproxy/haproxy_cch.cfg")
  }
}
