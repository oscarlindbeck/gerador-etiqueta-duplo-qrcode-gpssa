from models import notifications, qrcode, description, layout, pdf
import pandas as pd
import glob
import os


# Path of directory
path = os.getcwd()

# Path of file
file = glob.glob(f'{path}\\input\\*.xlsx')

# File reading
df = pd.read_excel(file[0])

# Position of components
page_pos = {1: [(280, 241), (208, 778), (562, 975)],
            2: [(1041, 241), (969, 778), (1323, 975)],
            3: [(1802, 241), (1730, 778), (2084, 975)],
            4: [(280, 1356), (208, 1893), (562, 2090)],
            5: [(1041, 1356), (969, 1893), (1323, 2090)],
            6: [(1802, 1356), (1730, 1893), (2084, 2090)],
            7: [(280, 2471), (208, 3008), (562, 3205)],
            8: [(1041, 2471), (969, 3008), (1323, 3205)],
            9: [(1802, 2471), (1730, 3008), (2084, 3205)]}

# Notifications
notify = notifications.Notifications(path, 'long')
# Start notification
notify.start()

# Start page index
page = 0

# Indicator of tag
indicator = 1

# Image list
image_list = []

for i in df.index:
    if indicator == 1:
        print(f'página {page}')

        image_list.append(f'{page}.png')

    # Create qrcodes
    qr = qrcode.QRCode(df['link main'][i], df['link secondary'][i])
    qr.create_qrcode_main()
    qr.create_qrcode_secondary()

    # Create description
    descr = description.Description(df['description'][i])
    descr = descr.create_description()

    # Create layout
    lay = layout.Layout(indicator, page, page_pos[indicator][0], page_pos[indicator][1], page_pos[indicator][2])
    lay.insert_qrcode_main()
    lay.insert_description(descr)
    lay.insert_qrcode_secondary()
    # Save png
    lay.save(page)

    print(f'{df["link main"][i]} inserido na {indicator}º posição')

    if indicator == 9:
        page = page + 1

        indicator = 0

    indicator = indicator + 1

# Generate pdf
pdf = pdf.PDF(path, image_list, 'qrcodes')
pdf.create()

# End notification
notify.finish()
