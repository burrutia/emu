class cron_solr_slv {
    file { "/var/spool/cron/web_user":
      owner => 'web_user',
      group => 'root',
      mode => 0600,
      content => template("/etc/puppet/manifests/templates/ssx/solr/cron/web_user_slv_cron")
     }
}

class cron_solr_master {
    file { "/var/spool/cron/web_user":
      owner => 'web_user',
      group => 'root',
      mode => 0600,
      content => template("/etc/puppet/manifests/templates/ssx/solr/cron/web_user_mst_cron")
     }
}
