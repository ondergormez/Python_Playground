

TODO: Tüm dosyaları yeniden oluştur.

```
# TODO: gerekli değilse sil. Uninstall et
 pip3 install ecdsa
```

* Private/Public Key Pair oluşturulur.
```sh
openssl ecparam -name secp256k1 -genkey -out privateKey.pem
openssl ec -in privateKey.pem -pubout -out publicKey.pem
```

* Private tarafıyla mesaj imzalanır.
```sh
openssl dgst -sha256 -sign privateKey.pem -out signatureDer.txt data.txt

# For converting to Der to Base64
openssl base64 -in signatureDer.txt -out signatureBase64.txt
```
