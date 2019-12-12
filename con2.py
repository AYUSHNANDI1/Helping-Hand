import tarfile
import os

opf="new.tar"
src="/tmp/Practice_Ayush/production/"
def make_tarfile(opf,src):
    with tarfile.open(opf, "w:gz") as tar:
        tar.add(src, arcname=os.path.basename(src))
    tar.close()
make_tarfile(opf,src)
