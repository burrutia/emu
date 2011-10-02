class check_page_err {
file { "/usr/lib/nagios/plugins/check_page_error.py":
    owner => 'root',
    group => 'root',
    mode => 0755,
    content => template("/etc/puppet/manifests/templates/mon/usr/lib/nagios/plugins/check_page_error.py")
   }
}
