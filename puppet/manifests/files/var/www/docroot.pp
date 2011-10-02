class docroot
{
  file {["/var/www"]:
    mode => "0755",
    owner => "web_user",
    group => "web_user",
    ensure => directory
    }
}

class dhtml_dir
{
  file {["/var/www/html"]:
    mode => "0755",
    owner => "web_user",
    group => "web_user",
    ensure => directory
    }
}
