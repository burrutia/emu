
class mail_perms { include clientmqueue }


class clientmqueue
{
file { ["/var/spool/clientmqueue"]:
 mode => "770",
 owner => "smmsp",
 group => "smmsp",
 ensure => directory
 }
}


