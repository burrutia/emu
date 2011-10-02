
class mnt_idir {
   file {["/images"]:
   owner => 'web_user',
   group => 'web_user',
   mode => '0755',
   ensure => directory
   }
}

class db_bakup_dir {
file {[ "/data", "/data/mysql", "/data/mysql/backups" ]:
   owner => 'dba',
   group => 'dba',
   mode => '0755',
   ensure => directory
  }
}

class mnt_img_web {
   $nfs_server = extlookup("ec2_filer")
   mount { "/images":
   device => "$nfs_server:/filer/share/images",
   ensure => "mounted",
   fstype => "nfs",
   options => "defaults",
   require => File["/images"],
   }
}

class mnt_media_ro {
   $nfs_server = extlookup("ec2_filer")
   mount { "/filer/vol1/shared/media":
   device => "$nfs_server:/vol1/share/dev_media",
   ensure => "mounted",
   fstype => "nfs",
   options => "ro,soft,rsize=32768,wsize=32768",
   }
}

