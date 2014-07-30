/*
	This will ensure that the exec is run before any package, 
	not that the exec is run before each package. 
*/
exec { "apt-update":
    command => "/usr/bin/apt-get update"
}

Exec["apt-update"] -> Package <| |>

# curl is needed to make the HTTP requests
package { "curl":
    ensure => "installed"
}

# required for ab
package { "apache2-utils":
	ensure => "installed"
}

class { 'nginx': }

nginx::resource::vhost { 'ab':
	www_root => '/vagrant/www/',
	listen_port => 81
}

class { 'apache': 
	#confd_dir => '/vagrant/manifests/modules/apache/files/',
}

apache::vhost { 'apache':
	#port => 8201,
	default_vhost => true,
 	docroot => '/vagrant/www',
 	#docroot_owner => 'www-data',
  	#docroot_group => 'www-data',
}
