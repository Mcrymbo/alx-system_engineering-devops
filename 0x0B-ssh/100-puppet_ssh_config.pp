# Used for updating configuaration file

include stdlib

file_line { 'Identity file':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  line    => '    IdenityFile ~/.ssh/school',
  replace => true,
}

file_line { 'password':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  replace => true,
}
