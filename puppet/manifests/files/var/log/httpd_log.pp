class httpd_log_dir {
    file { "/var/log/httpd":
       owner => 'web_user',
       group => 'web_user',
       mode => 0755,
       ensure => directory
    }
}
