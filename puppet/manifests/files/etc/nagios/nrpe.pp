class nrpe_config {
  file {"/etc/nagios/nrpe.cfg":
    owner => "root",
    group => "root",
    mode => "0444",
    require => Package[nrpe],
    notify => Service[nrpe],
    content =>template("/etc/puppet/manifests/templates/all/etc/nagios/nrpe.cfg")
    }
}
