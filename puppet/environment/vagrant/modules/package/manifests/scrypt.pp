### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class package::scrypt {
    require python

    ## local variables
    $hiera_dev = hiera('development')
    $version   = $hiera_dev['pip']['scrypt']

    package { 'scrypt':
        ensure   => $version,
        provider => 'pip',
    }
}
