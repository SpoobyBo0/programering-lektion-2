år = int(input("Hur många år är du?"))
månader = int(input("Hur många månader är du?"))

sekunderår = år*31536000
sekundermånader = månader*2629800

print(f"Du sa att du var {år} gammal och {månader} gammal det gör att du är {sekunderår + sekundermånader} sekunder gammal")