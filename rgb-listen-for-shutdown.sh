#! /bin/sh

### BEGIN INIT INFO
# Provides:          lgb-listen-for-shutdown.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
### END INIT INFO

# If you want a command to always run, put it here

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting lgb-listen-for-shutdown.py"
    /usr/local/bin/lgb-listen-for-shutdown.py &
    ;;
  stop)
    echo "Stopping lgb-listen-for-shutdown.py"
    pkill -f /usr/local/bin/lgb-listen-for-shutdown.py
    ;;
  *)
    echo "Usage: /etc/init.d/lgb-listen-for-shutdown.sh {start|stop}"
    exit 1
    ;;
esac

exit 0
