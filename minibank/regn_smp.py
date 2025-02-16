

vekst_faktor = 1.1
legg_til = 15_000
penger_hvert_år = 15_000

for år in range(1,32):
	første_ledd = penger_hvert_år * 1.1 
	print(f"{år}:{round(første_ledd,1)}")
	penger_hvert_år = første_ledd + legg_til



