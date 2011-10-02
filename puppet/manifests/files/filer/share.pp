class nfs_export
{
  file {["/filer"]:
    mode => "0755",
    owner => "root",
    group => "root",
    ensure => directory
    }
}

class share_dir
{
  file {["/filer/share"]:
    mode => "0755",
    owner => "deploy",
    group => "deploy",
    ensure => directory
    }
}

