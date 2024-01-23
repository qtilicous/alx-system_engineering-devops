# File: 7-puppet_install_nginx_web_server.pp

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location = /redirect_me {
        return 301 http://www.redirected.com;
    }

    error_page 404 /404.html;
    location = /404.html {
        internal;
        return 404 'Ceci n\'est pas une page';
    }
}",
  notify  => Exec['nginx-restart'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure    => 'running',
  enable    => true,
}

# Notify the exec to restart Nginx when the configuration changes
exec { 'nginx-restart':
  command     => '/bin/systemctl restart nginx',
  refreshonly => true,
}
