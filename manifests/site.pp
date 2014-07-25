package { "curl":
    ensure => "installed"
}

package { "apache2-utils":
	ensure => "installed"
}

file { 
	content => "cd /vagrant/python-server/ && python -m SimpleHTTPServer"
}