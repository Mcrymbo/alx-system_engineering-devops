# Used for updating configuaration file

exec { 'echo':
  path    => 'usr/bin:/bin',
  command => 'echo "    IdentityFile ~/.ssh/school\n PasswordAuthentication no" >> /etc/ssh/ssh_conf',
  returns => [0,1],
}
