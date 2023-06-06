# Analýza příspěvků - README

Tento projekt provádí analýzu příspěvků a vizualizuje výsledky pomocí grafů.

## Instalace
1. Naklonujte tento repozitář na svůj počítač pomocí 'git clone <adresa-repozitáře>'.
2. Přejděte do kořenového adresáře projektu.

### Instalace závislostí

Je doporučeno vytvořit si virtuální prostředí pro izolaci závislostí.

1. Nainstalujte závislosti pomocí nástroje pip
    pip install -r requirements.txt


### Instalace závislostí

1. Přejděte do složky s programem
2. Spusťte program s požadovanými argumenty. Například:
    python main.py --input ./source --output ./target

### Jak otestovat funkčnost 
Pro testování takové úlohy bych provedl následující kroky:

1. Sestavil bych sadu testovacích dat s různými kombinacemi příspěvků v různých letech a měsíců. Každý příspěvek by měl obsahovat textový atribut s různou délkou.

2. Vytvořil bych testovací skripty, které volají funkce pro analýzu dat a ověřují, zda výstupy jsou správné. Například:
- Ověřil bych, zda počet příspěvků v jednotlivých týdnech každého roku je správně spočítán.
- Ověřil bych, zda průměrná délka textu příspěvků v jednotlivých týdnech každého roku je správně vypočítána.
- Spustil bych testy a zkontroloval výstupy, zda odpovídají očekávaným výsledkům.

Pokud je k dispozici automatizované testování (např. pomocí nástroje jako je pytest), lze tyto testy začlenit do procesu CI a spouštět je při každé změně kódu.

Je také důležité zvážit různé okrajové případy a neobvyklé situace, jako například prázdný vstup, chybně formátovaná data nebo neexistence očekávaných atributů, a zajistit, aby byly řádně ošetřeny.

V případě potřeby lze také použít nástroje pro profilování a sledování výkonu, abyste zjistili, zda analýza dat nevykazuje nějaká úzká místa výkonu, která by bylo třeba optimalizovat.





