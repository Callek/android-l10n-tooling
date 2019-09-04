import pygit2
repo = pygit2.Repository('mozilla-mobile/android-components')
if 'fork' not in list(r.name for r in repo.remotes):
  fork_remote = repo.remotes.create('fork', 'ssh://git@github.com/Callek/android-components')
else:
  fork_remote = repo.remotes['fork']

class MyRemoteCallbacks(pygit2.RemoteCallbacks):
    def credentials(self, url, username_from_url, allowed_types):
        if allowed_types & pygit2.credentials.GIT_CREDTYPE_USERNAME:
            return pygit2.Username("git")
        elif allowed_types & pygit2.credentials.GIT_CREDTYPE_SSH_KEY:
            return pygit2.Keypair("git", "ssh_key.pub", "ssh-key", "")

"""
>>> fork_remote.push(['HEAD'], callbacks=MyRemoteCallbacks())
### CTRL^C
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.7/site-packages/pygit2/remote.py", line 487, in push
    check_error(err)
  File "/usr/local/lib/python3.7/site-packages/pygit2/errors.py", line 64, in check_error
    raise GitError(message)
_pygit2.GitError: Failed to authenticate SSH session: Unable to extract public key from private key file: Method unimplemented in libgcrypt backend
"""