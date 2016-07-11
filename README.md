# monitor

monitor program that performs contact actions should certain conditions, such as non-interaction, arise

# introduction

The script `monitor.py` imports a payload module. It attempts to send all of the e-mail messages in the messages list of the payload module should non-interaction be detected.

# setup

## LXPLUS ATLAS

```Bash
ssh "${USER}"@lxplus7.cern.ch
setupATLAS

echo "create Python virtual environment"
virtual_environment_name="virtual_environment"
virtualenv "${virtual_environment_name}"

echo "make activation dynamic"
activate_filename="virtual_environment/bin/activate"
temporary_filename="/tmp/"$(date "+%Y-%m-%dT%H%MZ" --utc)"" #"$(tempfile)"
cat > "${temporary_filename}" << "EOF"
directory_bin="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
directory_env="$(dirname "${directory_bin}")"
VIRTUAL_ENV="${directory_env}"
EOF
sed -i "/^VIRTUAL_ENV.*/ {
   r ${temporary_filename}
   d
}" "${activate_filename}"
rm "${temporary_filename}"

echo "activate Python virtual environment"
source "${virtual_environment_name}"/bin/activate

IFS= read -d '' text << "EOF"
import sys
reload(sys)
sys.setdefaultencoding("utf8")
EOF
echo "${text}" > "${virtual_environment_name}"/lib/python2.7/site-packages/sitecustomize.py

echo "install software in Python virtual environment"
pip install propyte

echo "make Python virtual environment relocatable"
virtualenv --relocatable virtual_environment
```