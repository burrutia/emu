# mta perms of rwxr-sr-x
class mta_perm {
file {"/usr/sbin/sendmail.sendmail":
    owner => 'root',
    group => 'smmsp',
    mode => 2755
    }
}
