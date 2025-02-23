import os
from PIL import Image

# Saadame praeguse kataloogi
current_directory = os.getcwd()

# Läbime kõik failid kataloogis
for filename in os.listdir(current_directory):
    # Kontrollime, kas fail on .webp
    if filename.endswith('.webp'):
        # Loeme .webp faili
        img = Image.open(filename)
        
        # Muudame faili nime, asendame .webp .jpg'ga
        new_filename = filename.replace('.webp', '.jpg')
        
        # Salvestame pildi .jpg formaadis
        img.convert('RGB').save(new_filename, 'JPEG')
        # print(f'{filename} konverteeritud {new_filename}')
        print('{} konverteeritud {}'.format(filename, new_filename))


print('Konverteerimine lõppenud!')
