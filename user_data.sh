  #!/bin/bash

DB_USER=admin
DB_PASS=
DB_HOST=
DB_PORT=3306
DB_NAME=weather
BUCKET_NAME=


######## DO NOT TOUCH ##########

echo '#!/bin/bash' > env.sh
echo 'DB_USER='$DB_USER >> env.sh
echo 'DB_PASS='$DB_PASS >> env.sh 
echo 'DB_HOST='$DB_HOST >> env.sh 
echo 'DB_PORT='$DB_PORT >> env.sh 
echo 'DB_NAME='$DB_NAME >> env.sh
echo 'BUCKET_NAME='$BUCKET_NAME >> env.sh
chmod +x env.sh

wget https://mintendo-programmer.de/files/bin/weather-webserver -O weather-webserver
wget https://mintendo-programmer.de/files/bin/weather-ghtml.tar.gz -O weather-ghtml.tar.gz
tar xvzf weather-ghtml.tar.gz
chmod +x weather-webserver

wget https://raw.githubusercontent.com/thimo-wellner/aws/master/webserver.service -O /etc/systemd/system/webserver.service
chmod 644 /etc/systemd/system/webserver.service
sudo systemctl start webserver
sudo systemctl enable webserver

######## DO NOT TOUCH ##########
