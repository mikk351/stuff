#!/bin/bash

#MONGO_HOST="127.0.0.1"
#MONGO_PORT="27017"

MONGO_DB="metaradDB"
TIME=$(date +"%m-%d-%Y")
BACKUP_NAME="DBdump_"$TIME
DUMP_DIR="/home/mikk/backups/mongoDump"

/usr/bin/mongodump --db $MONGO_DB --out $DUMP_DIR/$BACKUP_NAME
echo /usr/bin/mongodump --db $MONGO_DB --out $DUMP_DIR/$BACKUP_NAME
