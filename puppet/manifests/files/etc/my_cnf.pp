class mysql_mcnf {
 file { "/etc/my.cnf":
  owner => 'root',
  group => 'root',
  mode => '0644',
  content => template("/etc/puppet/manifests/templates/db/etc/my.cnf")
  }
}

class master_cnf {
 file { "/etc/my.cnf":
  owner => 'root',
  group => 'root',
  mode => '0644',
  notify => Service[mysql],
  content => template("/etc/puppet/manifests/templates/db/master/my.cnf")
  }
}

class master_cnf_ssl {
 file { "/etc/my.cnf":
  owner => 'root',
  group => 'root',
  mode => '0644',
  notify => Service[mysql],
  content => template("/etc/puppet/manifests/templates/db/master/my.cnf.ssl")
  }
}

class slave_cnf {
 file { "/etc/my.cnf":
  owner => 'root',
  group => 'root',
  mode => '0644',
  notify => Service[mysql],
  content => template("/etc/puppet/manifests/templates/db/slave/my.cnf")
  }
}
