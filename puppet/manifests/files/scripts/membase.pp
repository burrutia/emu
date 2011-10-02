# membase_init.sh

class membase_configure {
    include membase_init
    include membase_sinit
}


class membase_init {
    file { "/scripts/membase_init.sh":
    owner => "root",
    group => "root",
    mode => 0755,
    require => File["/scripts"],
    content => template("/etc/puppet/manifests/templates/cch/scripts/membase_init.sh")
    }
}

class membase_sinit {
    file { "/scripts/membase_init_slv.sh":
    owner => "root",
    group => "root",
    mode => 0755,
    require => File["/scripts"],
    content => template("/etc/puppet/manifests/templates/cch/scripts/membase_init_slv.sh")
    }
}

class membase_pcfg {
exec {"membase_pcfg":
   cwd => "/scripts",
   command => '/bin/bash /scripts/membase_init.sh',
   require => File["/scripts/membase_init.sh"],
  }
}

class membase_scfg {
exec {"membase_scfg":
   cwd => "/scripts",
   command => '/bin/bash /scripts/membase_init_slv.sh',
   require => File["/scripts/membase_init_slv.sh"],
  }
}
