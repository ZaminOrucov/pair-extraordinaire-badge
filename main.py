import time

def oyun_basla():
    print("====================================")
    print("  MİNİ SUAL-CAVAB OYUNUNA XOŞ GƏLDİNİZ!  ")
    print("====================================\n")
    time.sleep(1)
    
    suallar = [
        {
            "sual": "Azərbaycanın paytaxtı haradır?",
            "variantlar": "A) Gəncə  B) Bakı  C) Sumqayıt  D) Şəki",
            "cavab": "B"
        },
        {
            "sual": "Python proqramlaşdırma dili hansı ildə yaradılıb?",
            "variantlar": "A) 1991  B) 2000  C) 1985  D) 2010",
            "cavab": "A"
        },
        {
            "sual": "Dünyada ən böyük okean hansıdır?",
            "variantlar": "A) Atlantik  B) Hind  C) Sakit  D) Şimal Buzlu",
            "cavab": "C"
        },
        {
            "sual": "Suyun kimyəvi formulu hansıdır?",
            "variantlar": "A) CO2  B) H2O  C) NaCl  D) O2",
            "cavab": "B"
        },
        {
            "sual": "Leonardo Davinchi kimdir?",
            "variantlar": "A)Şair  B) Yazar  C) rəssam  D) qitara ifaçısı",
            "cavab": "B"
        }
    ]
    
    xal = 0
    sual_nomresi = 1
    
    for s in suallar:
        print(f"Sual {sual_nomresi}: {s['sual']}")
        print(s['variantlar'])
        
        istifadeci_cavabi = input("Cavabınızı daxil edin (A, B, C və ya D): ").strip().upper()
        
        if istifadeci_cavabi == s['cavab']:
            print("🎉 Təbriklər! Doğru cavab.\n")
            xal += 10  
        else:
            print(f"❌ Səhvdir. Düzgün cavab {s['cavab']} variantı idi.\n")
            
        sual_nomresi += 1
        time.sleep(0.5) 
        
    print("====================================")
    print("             OYUN BİTDİ!            ")
    print(f"Yekun xalınız: {xal} / {len(suallar) * 10}")
    print("====================================")

if __name__ == "__main__":
    oyun_basla()
