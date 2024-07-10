# Install 'flask' using Puppet

package { 'python3.8':
  ensure   => 'present'
}

package { 'python3-pip':
  ensure   => 'presnet'
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip']
}

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['flask']
}
