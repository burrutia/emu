class opt_yum {
 file {"/etc/yum.conf":
  owner => "root",
  group => "root",
  mode => 0644,
  content => template("/etc/puppet/manifests/templates/all/etc/yum.conf")
 }
}
