# meme-generator

opis:

aplikacija omogoča generiranje mema z spodnjim in zgornjim tekstom. Preko obrazca je mogoče podati zgornji in spodnji tekst ter naložiti sliko. Z klikom na gumb se generira meme in se prikaže v brskalniku.



navodila za zagon z dockerjem:

1. naložite datoteke iz repozitorija ali uporabite git clone
2. če še niste, si naložite docker
3. uporabite ukaz docker build -t meme-generator .
4. uporabite ukaz docker run -p 5000:5000 meme-generator za zagon docker kontejnerja
5. Opcijsko: preverite, če kontejner teče z ukazom docker ps
6. V brskalniku lahko dostopate do aplikacije na vratih 5000
