#
class gitweb
{
   include "gitweb_dir"
}

class gitweb_dir
{
 file {"/var/www/gitweb":
      owner => "root",
      group => "root",
      purge => true,
      recurse => true,
      force => true,
      source => "puppet:///files/git/var/www/gitweb"
      }
}

