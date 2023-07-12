# Virtual Environment(Sanal Ortam) and Package Management(Paket Yönetimi)

## Conda
# Sanal Ortamların listelenmesi :
# conda env list : Bilgisayarınızda varsa yüklü olan sanal ortamlar listenicektir.

# Sanal ortam oluşturma :
# conda create -n myenv

# sanal ortamı aktif hale getir.
# conda activate myenv

# sanal ortamdaki yüklü paketlerin listelenmesi :
# conda list

# paket yükleme :
# conda install numpy pandas scipy / paketler arasında bir boşluk bırakarak birden fazla inderebilirsin.

# paket silme :
# conda remove package_name

# Belirli bir versiyona göre paket yükleme :
# conda install numpy=1.20.1

# paket yükseltme :
# conda upgrade numpy

# Tüm paketlerin güncellenmesi :
# conda upgrade -all

# paket yükleme :
# pip install pandas==1.2.1

# ilgili paketlerin listesini sunuma hazırlamak :
# conda env export > environment.yaml

# pip için requirements.txt yaygındır.

# Sıfırdan environment oluşturma :
# conda env create -f environment.yaml