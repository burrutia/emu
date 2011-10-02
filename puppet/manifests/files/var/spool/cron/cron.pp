class cron_root {
    file {"/var/spool/cron/root":
      owner => 'root',
      group => 'root',
      mode => '0600',
      content => template("/etc/puppet/manifests/templates/all/var/spool/cron/root")
     }
}
