### Note: the prefix 'compiler::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class compiler::webcompilers {
    ## variables
    $root_dir        = '/vagrant'
    $environment     = 'development'
    $module          = 'compiler'
    $environment_dir = "${root_dir}/puppet/environment/${environment}"
    $compiler_dir    = "${environment_dir}/modules/${module}/scripts"
    $template_path   = 'compiler/webcompilers.erb'

    $compilers = [
        'browserify',
        'imagemin',
        'sass',
        'uglifyjs'
    ]

    ## define compilers
    $compilers.each |String $compiler| {
        ## dos2unix upstart: convert clrf (windows to linux) in case host
        #                    machine is windows.
        file { "/etc/init/${compiler}.conf":
            ensure  => file,
            content => dos2unix(template($template_path)),
        }

        ## dos2unix upstart: convert clrf (windows to linux) in case host
        #                    machine is windows.
        file { "${compiler_dir}/${compiler}":
            ensure  => file,
            content => dos2unix(template("${compiler_dir}/${compiler}")),
        }
    }
}