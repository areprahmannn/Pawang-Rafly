import pandas as pd

data = {
    'nama': ['Andi', 'Budi', 'Citra', 'Dewi', 'Eka'],
    'nilai_matematika': [78, 85, 90, 65, 88],
    'nilai_sains': [80, 82, 95, 60, 92],
    'nilai_bahasa': [75, 88, 85, 60, 90]
}

df = pd.DataFrame(data)

df['rata_rata'] = df[['nilai_matematika', 'nilai_sains', 'nilai_bahasa']].mean(axis=1)

murid_tertinggi = df.loc[df['rata_rata'].idxmax(), 'nama']
nilai_tertinggi = df['rata_rata'].max()

rata_matematika = df['nilai_matematika'].mean()
rata_sains = df['nilai_sains'].mean()
rata_bahasa = df['nilai_bahasa'].mean()

df_nama_index = df.set_index('nama')
print("=== DataFrame dengan index nama murid ===")
print(round(df_nama_index, 2))
print("\n")

print("Murid dengan rata-rata tertinggi:", murid_tertinggi, f"({nilai_tertinggi})\n")
print("Rata-rata Matematika:", rata_matematika)
print("Rata-rata Sains:", rata_sains)
print("Rata-rata Bahasa:", rata_bahasa)
print("\n")