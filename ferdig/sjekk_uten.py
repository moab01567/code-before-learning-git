import time
import epost_mot


forx_par = ["0"]

for i in forx_par:
	with open(f"valutaer/{i}_size.txt","w") as s:
		s.write("1")
	with open(f"{i}balance.txt","w") as b:
		b.write("0")
	with open("status.txt", "w") as st:
		st.write("aktiv")
	with open("status2.txt", "w") as st2:
		st2.write("ikke aktiv")
	with open("status3.txt","w") as w:
		status = w.write("ikke aktiv")
	with open("konto.txt","w") as k:
		k.write("1000")



	epost_mot.Start_up(i)



