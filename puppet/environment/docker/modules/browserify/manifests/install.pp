###
### install.pp, install browserify
###
class browserify::install {
    ## local variables
    $node_version       = $::browserify::node_version
    $browserify_version = $::browserify::browserify_version
    $babel_core_version = $::browserify::babel_core_version
    $babelify_version   = $::browserify::babelify_version
    $root_dir           = $::browserify::root_dir
    $directories        = [
        "${root_dir}/log",
        "${root_dir}/log/webcompiler",
    ]

    ## install nodejs, with npm
    class { 'nodejs':
        repo_url_suffix => $node_version,
    }

    ## install browserify related compilers
    package { 'babel-core': 
        ensure          => $babel_core_version,
        provider        => 'npm',
        require         => Class['nodejs'],
    }

    package { 'babelify': 
        ensure          => $babelify_version
        provider        => 'npm',
        require         => Class['nodejs'],
    }

    package { 'browserify': 
        ensure          => $node_browserify_version,
        provider        => 'npm',
        require         => Class['nodejs'],
    }
}
