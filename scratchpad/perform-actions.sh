set -ex
virtualenv --system-site-packages tooling
source tooling/bin/activate
pip install -U pip
pip install taskcluster

<< 
    import taskcluster
    tc_secrets = taskcluster.Secrets(taskcluster.optionsFromEnvironment())
    print(tc_secrets.get('project/releng/callek/github-bot-ssh')['secret']['ssh'], file=<fileobj>)



git clone https://github.com/mozilla-l10n/android-l10n

# TO ANDROID l10n
# ------------------
# one of
target =  mozilla-mobile/android-components
# target = mozilla-mobile/fenix

branch = $(basename ${target})-quarantine

create-l10n-branch --pull --repo ${target} --branch ${branch} android-l10n/

# If repo/branch is *ahead* do:
# git push fork -f .. ?  see scratchpad/push-to-fork.py
# create PR via API

# --------------------------

# FROM ANDROID L10n
# --------------------
# one of
target =  mozilla-mobile/android-components
# target = mozilla-mobile/fenix

git clone https://github.com/${target} ${target}

import-android-l10n android-l10n/mozilla-mobile/android-components/l10n.toml mozilla-mobile/android-components

# if repo/branch is *ahead* do:
# git push fork ... ? see scratchpad/push-to-fork.py
# create PR via API
