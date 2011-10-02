class user::qavirtual {

         @user { "qa_user1":
         ensure  => "present",
         uid     => "20050",
         gid     => "2000",
         password => '$2$fBg/4Ov$xp//UuSdedNxdde',
         comment  => "QA user 1",
         home => "/home/qa_user1",
         shell=> "/bin/bash",
         managehome => "true"
         }
         @user { "qa_user2":
         ensure  => "present",
         uid     => "20051",
         gid     => "2000",
         password => '$1$eQSWdJuQacSDcYg5fr/BvC.L3',
         home => "/home/qa_user2",
         comment  => "QA user 2",
         shell=> "/bin/bash",
         managehome => "true"
         }
}
