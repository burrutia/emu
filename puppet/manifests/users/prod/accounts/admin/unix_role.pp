class users::unix {
    @group { wheel:
        gid    => 10,
        ensure => present,
    }

}

