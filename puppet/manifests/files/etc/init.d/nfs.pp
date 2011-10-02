class nfsd {
   file { "/etc/init.d/nfs":
       owner => 'root',
       group => 'root',
       mode => 0755,
       notify => Service[nfs],
       content => template("/etc/puppet/manifests/templates/fs/etc/nfs")
   }
}
