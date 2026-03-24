A Relação: 
Existe uma relação claramente linear e crescente entre a entropia e o número de bits/byte no ficheiro comprimido.


O Significado da Entropia: 
A entropia dita a "desordem" ou a quantidade de informação útil de um ficheiro. Ficheiros com baixa entropia (como os nossos .txt ou o ficheiro de zeros a.txt) têm muita redundância, logo o compressor consegue baixar imenso os bits por byte.

Ficheiros Incompressíveis: 
Ficheiros com entropia muito perto de 8 (como o .jpg ou um ficheiro que já esteja comprimido) são praticamente "ruído aleatório". O compressor não consegue encontrar padrões neles, por isso a compressão obtida fica perto (ou até ligeiramente acima) de 8 bits/byte. Não há milagres! A linha azul tracejada prova isso mesmo: não se consegue comprimir um ficheiro para um tamanho menor do que a sua Entropia (Teorema de Shannon).