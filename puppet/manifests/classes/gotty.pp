# Setting up https://github.com/yudai/gotty
class gotty {
    $USER = 'vagrant'
    $GOTTY_DIR = "/home/$USER/gotty"

    file { "$GOTTY_DIR":
        ensure => 'directory',
        owner  => 'vagrant',
        group  => 'vagrant',
    }

    archive { "gotty":
        ensure => present,
        follow_redirects => true,
        checksum => false,
        url => "https://github.com/yudai/gotty/releases/download/v0.0.12/gotty_linux_amd64.tar.gz",
        user => "$USER",
        target => "$GOTTY_DIR",
        src_target => "$GOTTY_DIR",
        require => File["$GOTTY_DIR"]
    }
}
