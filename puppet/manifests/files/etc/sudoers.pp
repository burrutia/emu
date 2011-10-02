# sudoers recipes
class sudo_web {
file {"/etc/sudoers":
   owner => 'root',
   group => 'root',
   mode => '0440',
   content => template("/etc/puppet/manifests/templates/web/etc/web_sudoers")
   }
}
