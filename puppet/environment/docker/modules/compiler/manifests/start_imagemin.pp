### Note: the prefix 'compiler::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class compiler::start_imagemin {
    # variables
    $hiera_general   = hiera('general')
    $root_dir        = $hiera_general['root']
    $environment     = $hiera_general['environment']
    $dev_env_path    = "${root_dir}/puppet/environment/${environment}"

    # manually compile
    exec { 'imagemin':
        command  => "./imagemin ${root_dir}",
        cwd      => "${dev_env_path}/modules/compiler/scripts",
        provider => shell,
    }
}