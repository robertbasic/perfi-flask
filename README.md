perFi
=====

A Flask app for tracking personal finances. Mostly for learning Flask.
And to track my personal finances.

Install
=======

Intented to be run as a WSGI application under Apache.

    cd /var/www
    git clone git://github.com/robertbasic/perfi.git perfi
    cd perfi
    virtualenv venv
    source venv/bin/activate

Make sure to [pip install the dependencies!](#dependencies)

App config
----------

    cp appconfig.py.dist appconfig.py

And edit accordingly.

Database
--------

    cp perfi.sqlite.init perfi.sqlite

Apache
------

Apache needs to have enabled the WSGI module. Make sure the
`WSGISocketPrefix` path is set correctly in `wsgi.conf`.

Example vhost directive:

    <VirtualHost *:80>
        ServerAdmin webmaster@localhost

        ServerName perfi.local
        WSGIDaemonProcess perfi user=apache group=apache threads=5
        WSGIScriptAlias / /var/www/perfi/perfi.wsgi

        <Directory /var/www/perfi>
            WSGIScriptReloading On
            WSGIProcessGroup perfi
            WSGIApplicationGroup %{GLOBAL}
            Order deny,allow
            Allow from all
        </Directory>

        ErrorLog /var/log/httpd/perfi.local.error.log

        # Possible values include: debug, info, notice, warn, error, crit,
        # alert, emerg.
        LogLevel warn

        CustomLog /var/log/httpd/perfi.local.access.log combined

    </VirtualHost>

Dependencies<a id="dependencies"/>
============

 * flask
 * SQLAlchemy==0.8.0b2
 * WTForms==1.0.2
 * Flask-SQLAlchemy==0.16
 * Flask-Wtf==0.5
