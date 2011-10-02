# user virtual class for unix group
class user::unixvirtual {
         @user { "unix_user1":
         ensure  => "present",
         uid     => "10048",
         gid     => "10",
         password => '$1$7NkYu7Dg&6jd9/',
         comment  => "Unix user1",
         home => "/home/unix_user1",
         shell=> "/bin/bash",
         managehome => "true"
         }
         @user { "unix_user4":
         ensure  => "present",
         uid     => "10003",
         gid     => "10",
         password => '$1$uULN$YWEn2QMcM/LMEQVb98iUjG/1',
         comment  => "Unix user4",
         home => "/home/unix_user4",
         shell=> "/bin/bash",
         managehome => "true"
         }
         @user { "unix_user2":
         ensure  => "present",
         uid     => "10052",
         gid     => "10",
         password => '$1$HDMIsOjbf$NRNP/x$@$nju623Zd2/04',
         comment  => "Unix user2",
         home => "/home/unix_user2",
         shell=> "/bin/bash",
         managehome => "true"
         }
         @user { "unix_user3":
         ensure  => "present",
         uid     => "10032",
         gid     => "10",
         password => '$1$6PDmzu9v$KjKlf/ol9JK3eDUY/IK9',
         comment  => "Unix user3",
         home => "/home/unix_user3",
         shell=> "/bin/bash",
         managehome => "true"
         }
}

