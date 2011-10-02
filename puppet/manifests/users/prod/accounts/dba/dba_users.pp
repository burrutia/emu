class user::dbavirtual {
         @user { "dba":
         ensure  => "present",
         uid     => "867",
         gid     => "867",
         password => '$1$%qwe3ehDSHiSIN_XBU/N9OIM',
         comment => "Dba Role account",
         home => "/home/dba",
         shell=> "/bin/bash",
         managehome => "true"
         }
         @user { "dba_user1":
         ensure  => "absent",
         uid     => "10043",
         gid     => "867",
         password => '$1%xut/0$F/7rq98de0mLHeaXx9o0',
         comment => "Dba user1",
         home => "/home/dba_user1",
         shell=> "/bin/bash",
         managehome => "true"
         }
}

class group::dbavirtual {
         @group { "dba":
         ensure  => "present",
         gid     => "867",
         }
}
