class repl_access {
  include mysql_startup
  include replicant_sh
  include grant_slave_access
}


class scripts_dir {
    file { "/scripts":
    owner => "root",
    group => "root",
    mode => 0755,
    ensure => directory,
    }
}

class mysql_startup {
  file { "/scripts/startup.sh":
    owner => "root",
    group => "root",
    mode => 0755,
    content => template("/etc/puppet/manifests/templates/db/scripts/startup.sh")
    }
}

class replicant_sql {
  file { "/scripts/replicant_access.sql":
    owner => "root",
    group => "root",
    mode => 0755,
    content => template("/etc/puppet/manifests/templates/db/scripts/replicant_access.sql")
   }
}

class replicant_sh {
  file { "/scripts/replicant_access.sh":
    owner => "root",
    group => "root",
    mode => 0755,
    content => template("/etc/puppet/manifests/templates/db/scripts/replicant_access.sh")
   }
}

class grant_slave_access {
exec { "make_slave_access":
   cwd => "/scripts",
   command => "[ ! -f /scripts/slave ] && /bin/cat replicant_access.sh | /usr/bin/mysql && /bin/touch /scripts/slave",
   require => File["/scripts"],
   }
}

class make_slave {
  include slave_make
  include start_slave
}

class slave_make {
  file { "/scripts/make_slave.sql":
    owner => "root",
    group => "root",
    mode => 0755,
    content => template("/etc/puppet/manifests/templates/db/scripts/make_slave.sql")
   }
}

class start_slave {
exec { "slave_start":
   cwd => "/scripts",
   command => "[ ! -f /scripts/slave_made ] && /bin/cat make_slave.sql|/usr/bin/mysql && /bin/touch /scripts/slave_made && /usr/bin/mysql -e 'slave start'",
   unless => "[ -f /scripts/slave_made]",
   require => File["/scripts"],
   }
}

class clean_rgt_scale {
exec { "rm_rscale":
   cwd => "/scripts",
   command => "[ ! -f /scripts/rscale_removed ] && /bin/rpm -e rightscale --noscripts && /bin/touch /scripts/rscale_removed",
   unless => "[ -f /scripts/rscale_removed ]",
   require => File["/scripts"],
  }
}

class make_swapfile {
exec { "make_swapfile":
   cwd => "/scripts",
   command => "[ ! -f /mnt/swapfile001 ] && /bin/dd if=/dev/zero of=/mnt/swapfile001 bs=1M count=1K && /sbin/mkswap /mnt/swapfile001 &&  /sbin/swapon  /mnt/swapfile001",
   unless => '[  -f /mnt/swapfile001 ]',
   require => File["/scripts"],
  }
}

class swapon {
  exec {"swapon_swap_file":
   cwd => "/scripts",
   command => '[  -f /mnt/swapfile001 ] && CHECK_SWAP=$(/bin/cat /proc/swaps |/bin/grep [0-9]|/usr/bin/wc -l) &&  [ $CHECK_SWAP -lt 1 ] &&  /sbin/swapon  /mnt/swapfile001',
   unless => '[ -f /mnt/swapfile001 ] && CHECK_SWAP=$(/bin/cat /proc/swaps |/bin/grep [0-9]|/usr/bin/wc -l) &&  [ $CHECK_SWAP -eq 1 ]',
   require => File["/scripts"],
  }
}

