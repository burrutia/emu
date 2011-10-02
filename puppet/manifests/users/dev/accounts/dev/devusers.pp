# user virtual class for  dev group
class user::devvirtual {
         @user { "web_user":
         ensure  => "present",
         uid     => "2000",
         gid     => "2000",
         password => '$$e3d34e43rfwr+7S7X6YoQwNgujjn/',
         comment  => "Web User",
         home => "/home/web_user",
         shell=> "/bin/bash",
         managehome => "true"
         }
         @user { "dev_user1":
         ensure  => "present",
         uid     => "10036",
         gid     => "2000",
         password => '$$e3d34e43rfwr+7S7X6YoQwNgujjn/',
         comment  => "Web User 1",
         home => "/home/dev_user1",
         shell=> "/bin/bash",
         managehome => "true"
         }
         @user { "dev_user2":
         ensure  => "present",
         uid     => "10037",
         gid     => "2000",
         password => '$$e3d34e43rfwr+7S7X6YoQwNgujjn/',
         comment  => "Web User 2",
         home => "/home/dev_user2",
         shell=> "/bin/bash",
         managehome => "true"
         }
}


class group::devvirtual {
         @group { "web_user":
         ensure  => "present",
         gid     => "2000",
         }
}

