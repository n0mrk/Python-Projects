#!/bin/bash

today=`date '+%Y%m%d-%H:%M:%S'`;

~/Dropbox/Python/plex_backup_sync2.py    >> test_sync.log.$today      2>&1

#/plexmedia/backup_sync/man_sync.py       >> man_sync.log.$today       2>&1
#/plexmedia/backup_sync/family_sync.py    >> family_sync.log.$today    2>&1
#/plexmedia/backup_sync/goth_sync.py      >> goth_sync.log.$today      2>&1
#/plexmedia/backup_sync/billiards_sync.py >> billiards_sync.log.$today 2>&1



