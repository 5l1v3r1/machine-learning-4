### Note: the prefix 'system::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class system::webcompiler_directories {
    $directories = {
        browserify => {
            src       => 'jsx',
            asset     => 'js',
            asset_dir => true,
            src_dir   => true,
        },
        imagemin   => {
            src   => 'img',
            asset => 'img',
            asset_dir => true,
            src_dir   => true,
        },
        sass       => {
            src       => 'scss',
            asset     => 'css',
            asset_dir => true,
            src_dir   => true,
        },
        uglifyjs   => {
            src       => 'js',
            asset     => 'js',
            asset_dir => false,
            src_dir   => false,
        }
    }

    $directories.each |String $directory, Hash $compiler| {
        ## create asset directories (if not exist)
        if ($compiler['asset_dir']) {
            file { "/vagrant/interface/static/${compiler['asset']}/":
                ensure => 'directory',
            }
        }

        ## create src directories (if not exist)
        if ($compiler['src_dir']) {
            file { "/vagrant/src/${compiler['src']}/":
                ensure => 'directory',
            }
        }
    }
}