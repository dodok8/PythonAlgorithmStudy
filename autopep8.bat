for /r %%G in (*.py) do autopep8 --in-place --aggressive --aggressive "%%G"