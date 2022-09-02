run("mkdir /boot")
run("cp /tmp/nel/nel.py /boot/nel.py")
if os.path.exists(file("/boot/boot.conf")):
    pass
else:
    run("cp /tmp/nel/boot.conf /boot/boot.conf")

if os.path.exists(file("/boot.py")):
    pass
else:
    run("cp /tmp/nel/boot.py /boot.py")
