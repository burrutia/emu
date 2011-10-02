class asset_exports {
  file {"/etc/exports":
    owner => 'root',
    group => 'root',
    mode => '0644',
    content => template("/etc/puppet/manifests/templates/fs/etc/exports/exports")
   }
}
