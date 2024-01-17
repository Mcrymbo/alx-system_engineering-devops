# installing and configuring nginx
package { 'nginx':
  ensure => installed,
}

#adding redirect
file_line { 'redirect':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://github.com/Mcrymbo permanent;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => [Package['nginx'], File_line['redirect']],
}
