bedrag= int(input("het bedrag in cent: "))

twee_euro = bedrag // 200
rest = bedrag % 200

een_euro = rest // 100
rest = bedrag % 100

fijftig_cent = rest // 50
rest = rest % 50

twintig_cent = rest // 20
rest = rest % 20

tien_cent = rest // 10
rest = rest % 10

vijf_cent = rest // 5
rest = rest % 5

twee_cent = rest // 2
rest = rest % 2

een_cent = rest

print(twee_euro,"x 2eur,",een_euro,"x 1eur,", fijftig_cent,"x 0.50eur,",twintig_cent,"x 0.2eur,", tien_cent,"x 0.1eur,",vijf_cent,"x 0.05eur,", twee_cent,"x 0.02eur,",een_cent,"x 0.01eur,")
