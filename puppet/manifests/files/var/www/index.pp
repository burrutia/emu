
class fake_index {
 file {"/var/www/html/index.html":
  owner => 'web_user',
  group => 'web_user',
  mode => 0644,
  content => template("/etc/puppet/manifests/templates/www/var/www/html/index.html")
 }
}

