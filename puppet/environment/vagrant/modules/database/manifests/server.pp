### Note: the prefix 'database::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class database::server {
    ## local variables
    $hiera_general    = hiera('general')
    $hiera_database   = hiera('database')
    $host             = $hiera_general['host']
    $db               = $hiera_database['name']
    $db_user          = $hiera_database['username']
    $db_pass          = $hiera_database['password']
    $provisioner      = $hiera_database['provisioner']
    $provisioner_pass = $hiera_database['provisioner_password']
    $tester           = $hiera_database['tester']
    $tester_pass      = $hiera_database['tester_password']
    $root_pass        = $hiera_database['root_password']

    ## mysql::server: install, and configure mariadb-server
    #
    #  @password_hash, default password (can be adjusted via cli)
    #  @max_connections_per_hour, @max_queries_per_hour, @max_updates_per_hour,
    #      @max_user_connections, a zero value indicates no limit
    class { '::mysql::server':
        package_name  => 'mariadb-server',
        root_password => $root_pass,
        users         => {
            "${db_user}@${host}"     => {
                ensure                   => 'present',
                max_connections_per_hour => '0',
                max_queries_per_hour     => '0',
                max_updates_per_hour     => '0',
                max_user_connections     => '0',
                password_hash            => mysql_password($db_pass),
            },
            "${provisioner}@${host}" => {
                ensure                   => 'present',
                max_connections_per_hour => '1',
                max_queries_per_hour     => '0',
                max_updates_per_hour     => '0',
                max_user_connections     => '1',
                password_hash            => mysql_password($provisioner_pass),
            },
            "${tester}@${host}" => {
                ensure                   => 'present',
                max_connections_per_hour => '0',
                max_queries_per_hour     => '0',
                max_updates_per_hour     => '0',
                max_user_connections     => '1',
                password_hash            => mysql_password($tester_pass),
            },
        },
        grants        => {
            "${db_user}@${host}/${db}.*"     => {
                ensure     => 'present',
                options    => ['GRANT'],
                privileges => ['INSERT', 'DELETE', 'UPDATE', 'SELECT'],
                table      => "${db}.*",
                user       => "${db_user}@${host}",
            },
            "${provisioner}@${host}/${db}.*" => {
                ensure     => 'present',
                options    => ['GRANT'],
                privileges => ['INSERT', 'CREATE'],
                table      => "${db}.*",
                user       => "${provisioner}@${host}",
            },
            "${tester}@${host}/${db}.*" => {
                ensure     => 'present',
                options    => ['GRANT'],
                privileges => ['SELECT', 'DROP'],
                table      => "${db}.*",
                user       => "${tester}@${host}",
            },
        },
        databases     => {
            $db => {
                ensure  => 'present',
                charset => 'utf8',
            },
        },
    }
    contain mysql::server
}