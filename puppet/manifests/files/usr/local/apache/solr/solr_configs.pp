class solr_master {
file { "/usr/local/apache/solr/current/solr/conf/solrconfig.xml":
      owner => 'deploy',
      group => 'deploy',
      mode => 0664,
      content => template("/etc/puppet/manifests/templates/ssx/solr/conf/solrconfig.master.xml")
    }
}

class solr_mage_master {
file { "/usr/local/apache/solr/current/solr/conf/solrconfig.xml":
      owner => 'deploy',
      group => 'deploy',
      mode => 0664,
      content => template("/etc/puppet/manifests/templates/ssx/solr/conf/solrconfig_mage.master.xml")
    }
}

class solr_rsync_enable {
    include solr_sync_check
    include solr_log_dir
}

class solr_log_dir {
file { "/usr/local/apache/solr/current/solr/logs":
      owner => 'deploy',
      group => 'deploy',
      mode => 0755,
      ensure => directory
     }
}

class solr_sync_check {
  file {"/usr/local/apache/solr/current/solr/bin/rsyncd-check":
      owner => 'deploy',
      group => 'deploy',
      mode => 0755,
      content => template("/etc/puppet/manifests/templates/ssx/solr/cron/rsyncd-check")
      }
}


class solr_slave_tpl {
file { "/usr/local/apache/solr/current/solr/conf/solrconfig_slave.xml":
      owner => 'deploy',
      group => 'deploy',
      mode => 0664,
      content => template("/etc/puppet/manifests/templates/ssx/solr/conf/solrconfig_slave.xml")
    }
}

class solr_mage_slave_tpl {
file { "/usr/local/apache/solr/current/solr/conf/solrconfig_slave.xml":
      owner => 'deploy',
      group => 'deploy',
      mode => 0664,
      content => template("/etc/puppet/manifests/templates/ssx/solr/conf/solrconfig_mage.slave.xml")
    }
}

class solr_slave {
file { "/usr/local/apache/solr/current/solr/conf/solrconfig.xml":
      owner => 'deploy',
      group => 'deploy',
      mode => 0664,
      content => template("/etc/puppet/manifests/templates/ssx/solr/conf/solrconfig_slave2.xml")
    }
}

class solr_script_conf {
file {"/usr/local/apache/solr/current/solr/conf/scripts.conf":
      owner => 'deploy',
      group => 'deploy',
      mode => 0664,
      content => template("/etc/puppet/manifests/templates/ssx/solr/conf/scripts.conf")
      }
}
