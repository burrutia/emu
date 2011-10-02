class capistrano_ext
{
package {["capistrano-ext"]:
    provider => "gem",
    ensure => installed
  }
}


class capistrano
{
package {["capistrano"]:
    provider => "gem",
    ensure => installed
  }
}

class capistrano_deps
{
 include net_ssh_gw
 include highline
 include net_sftp
 include net_ssh
 include net_scp
}

class highline
{
package {["highline"]:
    provider => "gem",
    ensure => installed
  }
}

class net_ssh
{
package {["net-ssh"]:
    provider => "gem",
    ensure => installed
  }
}

class net_sftp
{
package {["net-sftp"]:
    provider => "gem",
    ensure => installed
  }
}

class net_scp
{
package {["net-scp"]:
    provider => "gem",
    ensure => installed
  }
}

class netssh_gateway
{
package {["net-ssh-gateway"]:
    provider => "gem",
    ensure => installed
  }
}
